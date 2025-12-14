from app.extensions import db
from datetime import datetime

class Volunteer(db.Model):
    __tablename__ = 'volunteers'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    interests = db.Column(db.Text)  # JSON array of interest areas
    availability = db.Column(db.String(500))
    skills = db.Column(db.Text)
    experience = db.Column(db.Text)
    why_volunteer = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'city': self.city,
            'country': self.country,
            'interests': self.interests,
            'skills': self.skills,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }