from app.extensions import db
from datetime import datetime

class Donation(db.Model):
    __tablename__ = 'donations'
    
    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('donors.id'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    currency = db.Column(db.String(3), default='USD')
    donation_type = db.Column(db.String(20), nullable=False)  # one-time, recurring
    frequency = db.Column(db.String(20))  # monthly, quarterly, yearly
    status = db.Column(db.String(20), default='pending')  # pending, completed, failed, refunded
    payment_method = db.Column(db.String(20))  # stripe, paypal
    payment_intent_id = db.Column(db.String(255), unique=True)
    transaction_id = db.Column(db.String(255), unique=True)
    honor_of = db.Column(db.String(255))
    dedication_message = db.Column(db.Text)
    is_anonymous = db.Column(db.Boolean, default=False)
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    donor = db.relationship('Donor', back_populates='donations')
    program = db.relationship('Program', back_populates='donations')
    
    def to_dict(self):
        return {
            'id': self.id,
            'donor_id': self.donor_id,
            'amount': float(self.amount),
            'currency': self.currency,
            'donation_type': self.donation_type,
            'frequency': self.frequency,
            'status': self.status,
            'payment_method': self.payment_method,
            'honor_of': self.honor_of,
            'is_anonymous': self.is_anonymous,
            'program_id': self.program_id,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }