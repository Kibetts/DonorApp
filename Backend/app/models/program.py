from app.extensions import db
from datetime import datetime

class Program(db.Model):
    __tablename__ = 'programs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    short_description = db.Column(db.String(500))
    category = db.Column(db.String(100))  # education, nutrition, healthcare, etc.
    image_url = db.Column(db.String(500))
    goal_amount = db.Column(db.Numeric(10, 2))
    raised_amount = db.Column(db.Numeric(10, 2), default=0.00)
    beneficiaries_count = db.Column(db.Integer, default=0)
    location = db.Column(db.String(255))
    status = db.Column(db.String(20), default='active')  # active, completed, paused
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    donations = db.relationship('Donation', back_populates='program')
    stories = db.relationship('Story', back_populates='program')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'description': self.description,
            'short_description': self.short_description,
            'category': self.category,
            'image_url': self.image_url,
            'goal_amount': float(self.goal_amount) if self.goal_amount else None,
            'raised_amount': float(self.raised_amount),
            'beneficiaries_count': self.beneficiaries_count,
            'location': self.location,
            'status': self.status,
            'is_featured': self.is_featured,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }