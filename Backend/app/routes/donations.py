from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.donation import Donation
from app.models.donor import Donor
from app.models.program import Program
from app.services.payment_service import PaymentService
from app.services.email_service import EmailService
from app.services.validation_service import ValidationService
from app.services.analytics_service import AnalyticsService

bp = Blueprint('donations_bp', __name__)

@bp.route('/', methods=['POST'])
def create_donation():
    """Create a new donation"""
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['first_name', 'last_name', 'email', 'amount', 'donation_type']
    is_valid, error = ValidationService.validate_required_fields(data, required_fields)
    if not is_valid:
        return jsonify({'error': error}), 400
    
    # Validate email
    is_valid, email = ValidationService.validate_email_address(data['email'])
    if not is_valid:
        return jsonify({'error': 'Invalid email address'}), 400
    
    # Validate amount
    is_valid, amount = ValidationService.validate_amount(data['amount'])
    if not is_valid:
        return jsonify({'error': amount}), 400
    
    try:
        # Get or create donor
        donor = Donor.query.filter_by(email=email).first()
        if not donor:
            donor = Donor(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=email,
                phone=data.get('phone'),
                address=data.get('address'),
                city=data.get('city'),
                state=data.get('state'),
                postal_code=data.get('postal_code'),
                country=data.get('country', 'US')
            )
            db.session.add(donor)
            db.session.flush()
        
        # Create donation record
        donation = Donation(
            donor_id=donor.id,
            amount=amount,
            currency=data.get('currency', 'USD'),
            donation_type=data['donation_type'],
            frequency=data.get('frequency'),
            payment_method=data.get('payment_method', 'stripe'),
            honor_of=data.get('honor_of'),
            dedication_message=data.get('dedication_message'),
            is_anonymous=data.get('is_anonymous', False),
            program_id=data.get('program_id'),
            status='pending'
        )
        db.session.add(donation)
        db.session.flush()
        
        # Process payment
        if donation.donation_type == 'recurring':
            payment = PaymentService.create_subscription(
                donor, amount, donation.currency, donation.frequency
            )
            donation.payment_intent_id = payment.id
        else:
            payment = PaymentService.create_payment_intent(
                amount, donation.currency, donor, donation.donation_type
            )
            donation.payment_intent_id = payment.id
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'donation_id': donation.id,
            'client_secret': payment.client_secret if hasattr(payment, 'client_secret') else None,
            'message': 'Donation created successfully'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:donation_id>/confirm', methods=['POST'])
def confirm_donation(donation_id):
    """Confirm a donation payment"""
    donation = Donation.query.get_or_404(donation_id)
    
    try:
        # Verify payment with Stripe
        is_confirmed = PaymentService.confirm_payment(donation.payment_intent_id)
        
        if is_confirmed:
            donation.status = 'completed'
            donation.transaction_id = donation.payment_intent_id
            
            # Update donor stats
            donor = donation.donor
            donor.total_donated += donation.amount
            donor.donation_count += 1
            if donation.donation_type == 'recurring':
                donor.is_monthly_donor = True
            
            # Update program stats if applicable
            if donation.program_id:
                program = Program.query.get(donation.program_id)
                if program:
                    program.raised_amount += donation.amount
            
            db.session.commit()
            
            # Send receipt email
            EmailService.send_donation_receipt(donor, donation)
            
            return jsonify({
                'success': True,
                'message': 'Donation confirmed',
                'donation': donation.to_dict()
            }), 200
        else:
            donation.status = 'failed'
            db.session.commit()
            return jsonify({'error': 'Payment verification failed'}), 400
            
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@bp.route('/stats', methods=['GET'])
def get_donation_stats():
    """Get donation statistics"""
    try:
        stats = AnalyticsService.get_impact_stats()
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/recent', methods=['GET'])
def get_recent_donations():
    """Get recent donations"""
    try:
        limit = request.args.get('limit', 10, type=int)
        donations = AnalyticsService.get_recent_donations(limit)
        return jsonify(donations), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/', methods=['GET'])
def list_donations():
    """List all donations (for admin)"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        donations = Donation.query\
            .order_by(Donation.created_at.desc())\
            .paginate(page=page, per_page=per_page, error_out=False)
        
        return jsonify({
            'donations': [d.to_dict() for d in donations.items],
            'total': donations.total,
            'pages': donations.pages,
            'current_page': page
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500