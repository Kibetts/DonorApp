from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.story import Story
from datetime import datetime

bp = Blueprint('stories_bp', __name__)

@bp.route('/', methods=['GET'])
def list_stories():
    """List all published stories"""
    try:
        featured_only = request.args.get('featured', 'false').lower() == 'true'
        category = request.args.get('category')
        limit = request.args.get('limit', type=int)
        
        query = Story.query.filter(Story.published_at.isnot(None))
        
        if featured_only:
            query = query.filter_by(is_featured=True)
        
        if category:
            query = query.filter_by(category=category)
        
        query = query.order_by(Story.published_at.desc())
        
        if limit:
            query = query.limit(limit)
        
        stories = query.all()
        
        return jsonify({
            'stories': [s.to_dict() for s in stories]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:story_id>', methods=['GET'])
def get_story(story_id):
    """Get a specific story"""
    story = Story.query.get_or_404(story_id)
    return jsonify(story.to_dict()), 200

@bp.route('/<string:slug>', methods=['GET'])
def get_story_by_slug(slug):
    """Get a story by slug"""
    story = Story.query.filter_by(slug=slug).first_or_404()
    return jsonify(story.to_dict()), 200