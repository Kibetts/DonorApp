from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.contact import ContactSubmission
from app.services.email_service import EmailService
from app.services.validation_service import ValidationService

bp = Blueprint('contact', __name__)

@bp.route('/submit', methods=['POST'])
def submit():
    """Submit contact form"""
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['name', 'email', 'subject', 'message']
    is_valid, error = ValidationService.validate_required_fields(data, required_fields)
    if not is_valid:
        return jsonify({'error': error}), 400
    
    # Validate email
    is_valid, email = ValidationService.validate_email_address(data['email'])
    if not is_valid:
        return jsonify({'error': 'Invalid email address'}), 400
    
    try:
        submission = ContactSubmission(
            name=data['name'],
            email=email,
            phone=data.get('phone'),
            subject=data['subject'],
            message=data['message']
        )
        
        db.session.add(submission)
        db.session.commit()
        
        # Send confirmation email
        EmailService.send_contact_confirmation(submission)
        
        return jsonify({
            'success': True,
            'message': 'Message sent successfully'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500