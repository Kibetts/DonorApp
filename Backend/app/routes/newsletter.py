from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.newsletter import NewsletterSubscriber
from app.services.email_service import EmailService
from app.services.validation_service import ValidationService

bp = Blueprint('newsletter_bp', __name__)

@bp.route('/subscribe', methods=['POST'])
def subscribe():
    """Subscribe to newsletter"""
    data = request.get_json()
    
    # Validate email
    if 'email' not in data:
        return jsonify({'error': 'Email is required'}), 400
    
    is_valid, email = ValidationService.validate_email_address(data['email'])
    if not is_valid:
        return jsonify({'error': 'Invalid email address'}), 400
    
    try:
        # Check if already subscribed
        existing = NewsletterSubscriber.query.filter_by(email=email).first()
        
        if existing:
            if existing.is_active:
                return jsonify({'message': 'Already subscribed'}), 200
            else:
                # Reactivate subscription
                existing.is_active = True
                existing.unsubscribed_at = None
                db.session.commit()
                return jsonify({'success': True, 'message': 'Subscription reactivated'}), 200
        
        # Create new subscriber
        subscriber = NewsletterSubscriber(
            email=email,
            first_name=data.get('first_name'),
            last_name=data.get('last_name')
        )
        
        db.session.add(subscriber)
        db.session.commit()
        
        # Send confirmation email
        EmailService.send_newsletter_confirmation(subscriber)
        
        return jsonify({
            'success': True,
            'message': 'Successfully subscribed to newsletter'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@bp.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """Unsubscribe from newsletter"""
    data = request.get_json()
    
    if 'email' not in data:
        return jsonify({'error': 'Email is required'}), 400
    
    try:
        subscriber = NewsletterSubscriber.query.filter_by(email=data['email']).first()
        
        if not subscriber:
            return jsonify({'error': 'Email not found'}), 404
        
        from datetime import datetime
        subscriber.is_active = False
        subscriber.unsubscribed_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Successfully unsubscribed'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500