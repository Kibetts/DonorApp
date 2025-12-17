from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.volunteer import Volunteer
from app.services.email_service import EmailService
from app.services.validation_service import ValidationService

bp = Blueprint('volunteers_bp', __name__)

@bp.route('/apply', methods=['POST'])
def apply():
    """Submit volunteer application"""
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['first_name', 'last_name', 'email', 'why_volunteer']
    is_valid, error = ValidationService.validate_required_fields(data, required_fields)
    if not is_valid:
        return jsonify({'error': error}), 400
    
    # Validate email
    is_valid, email = ValidationService.validate_email_address(data['email'])
    if not is_valid:
        return jsonify({'error': 'Invalid email address'}), 400
    
    try:
        volunteer = Volunteer(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=email,
            phone=data.get('phone'),
            address=data.get('address'),
            city=data.get('city'),
            state=data.get('state'),
            country=data.get('country'),
            interests=data.get('interests'),
            availability=data.get('availability'),
            skills=data.get('skills'),
            experience=data.get('experience'),
            why_volunteer=data['why_volunteer']
        )
        
        db.session.add(volunteer)
        db.session.commit()
        
        # Send confirmation email
        EmailService.send_volunteer_confirmation(volunteer)
        
        return jsonify({
            'success': True,
            'message': 'Volunteer application submitted successfully'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500