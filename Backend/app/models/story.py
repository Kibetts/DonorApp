from app.extensions import db
from datetime import datetime

class Story(db.Model):
    __tablename__ = 'stories'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.String(500))
    beneficiary_name = db.Column(db.String(255))
    beneficiary_age = db.Column(db.Integer)
    image_url = db.Column(db.String(500))
    before_image_url = db.Column(db.String(500))
    after_image_url = db.Column(db.String(500))
    video_url = db.Column(db.String(500))
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'))
    category = db.Column(db.String(100))  # success_story, testimonial, update
    is_featured = db.Column(db.Boolean, default=False)
    published_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    program = db.relationship('Program', back_populates='stories')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'content': self.content,
            'excerpt': self.excerpt,
            'beneficiary_name': self.beneficiary_name,
            'beneficiary_age': self.beneficiary_age,
            'image_url': self.image_url,
            'before_image_url': self.before_image_url,
            'after_image_url': self.after_image_url,
            'video_url': self.video_url,
            'program_id': self.program_id,
            'category': self.category,
            'is_featured': self.is_featured,
            'published_at': self.published_at.isoformat() if self.published_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }