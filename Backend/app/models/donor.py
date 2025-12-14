from app.extensions import db
from datetime import datetime

class Donor(db.Model):
    __tablename__ = 'donors'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    postal_code = db.Column(db.String(20))
    country = db.Column(db.String(100))
    stripe_customer_id = db.Column(db.String(255), unique=True)
    paypal_customer_id = db.Column(db.String(255), unique=True)
    total_donated = db.Column(db.Numeric(10, 2), default=0.00)
    donation_count = db.Column(db.Integer, default=0)
    is_monthly_donor = db.Column(db.Boolean, default=False)
    email_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    donations = db.relationship('Donation', back_populates='donor', lazy='dynamic')
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'city': self.city,
            'country': self.country,
            'total_donated': float(self.total_donated),
            'donation_count': self.donation_count,
            'is_monthly_donor': self.is_monthly_donor,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }