from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.program import Program

bp = Blueprint('programs_bp', __name__)

@bp.route('/', methods=['GET'])
def list_programs():
    """List all active programs"""
    try:
        featured_only = request.args.get('featured', 'false').lower() == 'true'
        category = request.args.get('category')
        
        query = Program.query.filter_by(status='active')
        
        if featured_only:
            query = query.filter_by(is_featured=True)
        
        if category:
            query = query.filter_by(category=category)
        
        programs = query.order_by(Program.created_at.desc()).all()
        
        return jsonify({
            'programs': [p.to_dict() for p in programs]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:program_id>', methods=['GET'])
def get_program(program_id):
    """Get a specific program"""
    program = Program.query.get_or_404(program_id)
    return jsonify(program.to_dict()), 200

@bp.route('/<string:slug>', methods=['GET'])
def get_program_by_slug(slug):
    """Get a program by slug"""
    program = Program.query.filter_by(slug=slug).first_or_404()
    return jsonify(program.to_dict()), 200

@bp.route('/', methods=['POST'])
def create_program():
    """Create a new program (admin only)"""
    data = request.get_json()
    
    try:
        program = Program(
            title=data['title'],
            slug=data['slug'],
            description=data['description'],
            short_description=data.get('short_description'),
            category=data.get('category'),
            image_url=data.get('image_url'),
            goal_amount=data.get('goal_amount'),
            location=data.get('location'),
            is_featured=data.get('is_featured', False)
        )
        
        db.session.add(program)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'program': program.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500