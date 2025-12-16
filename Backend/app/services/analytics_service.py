from sqlalchemy import func
from app.models.donation import Donation
from app.models.donor import Donor
from app.models.program import Program
from app.extensions import db
from datetime import datetime, timedelta

class AnalyticsService:
    
    @staticmethod
    def get_impact_stats():
        """Get overall impact statistics"""
        total_donations = db.session.query(
            func.sum(Donation.amount)
        ).filter(Donation.status == 'completed').scalar() or 0
        
        total_donors = db.session.query(
            func.count(Donor.id)
        ).scalar() or 0
        
        monthly_donors = db.session.query(
            func.count(Donor.id)
        ).filter(Donor.is_monthly_donor == True).scalar() or 0
        
        total_beneficiaries = db.session.query(
            func.sum(Program.beneficiaries_count)
        ).scalar() or 0
        
        return {
            'total_raised': float(total_donations),
            'total_donors': total_donors,
            'monthly_donors': monthly_donors,
            'children_helped': int(total_beneficiaries),
            'programs_active': Program.query.filter_by(status='active').count()
        }
    
    @staticmethod
    def get_recent_donations(limit=10):
        """Get recent donations"""
        donations = Donation.query\
            .filter(Donation.status == 'completed')\
            .filter(Donation.is_anonymous == False)\
            .order_by(Donation.created_at.desc())\
            .limit(limit)\
            .all()
        
        result = []
        for donation in donations:
            result.append({
                'amount': float(donation.amount),
                'donor_name': f"{donation.donor.first_name} {donation.donor.last_name[0]}.",
                'date': donation.created_at.isoformat(),
                'program': donation.program.title if donation.program else None
            })
        
        return result
    
    @staticmethod
    def get_donation_trends(days=30):
        """Get donation trends over time"""
        start_date = datetime.utcnow() - timedelta(days=days)
        
        donations = db.session.query(
            func.date(Donation.created_at).label('date'),
            func.sum(Donation.amount).label('total'),
            func.count(Donation.id).label('count')
        ).filter(
            Donation.created_at >= start_date,
            Donation.status == 'completed'
        ).group_by(
            func.date(Donation.created_at)
        ).all()
        
        return [{
            'date': str(d.date),
            'total': float(d.total),
            'count': d.count
        } for d in donations]
    
    @staticmethod
    def get_program_performance():
        """Get performance metrics for each program"""
        programs = Program.query.filter_by(status='active').all()
        
        result = []
        for program in programs:
            total_raised = db.session.query(
                func.sum(Donation.amount)
            ).filter(
                Donation.program_id == program.id,
                Donation.status == 'completed'
            ).scalar() or 0
            
            donation_count = db.session.query(
                func.count(Donation.id)
            ).filter(
                Donation.program_id == program.id,
                Donation.status == 'completed'
            ).scalar() or 0
            
            result.append({
                'program_id': program.id,
                'program_name': program.title,
                'total_raised': float(total_raised),
                'donation_count': donation_count,
                'goal_amount': float(program.goal_amount) if program.goal_amount else None,
                'progress_percentage': (float(total_raised) / float(program.goal_amount) * 100) 
                    if program.goal_amount and program.goal_amount > 0 else 0
            })
        
        return result