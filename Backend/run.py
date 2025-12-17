from app import create_app
from app.extensions import db
import os

# Create the app instance
app = create_app()

# Make app available for Flask CLI
def create_application():
    return app

@app.cli.command()
def init_db():
    """Initialize the database"""
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

@app.cli.command()
def seed_db():
    """Seed the database with sample data"""
    with app.app_context():
        from app.models import Program, Story
        from datetime import datetime
        
        # Create sample programs
        programs = [
            Program(
                title="Education for All",
                slug="education-for-all",
                description="Providing quality education to underprivileged children",
                short_description="Help us provide education to 500 children",
                category="education",
                image_url="/images/education.jpg",
                goal_amount=50000,
                raised_amount=35000,
                beneficiaries_count=350,
                location="Kenya",
                is_featured=True
            ),
            Program(
                title="Nutrition Program",
                slug="nutrition-program",
                description="Ensuring every child has access to nutritious meals",
                short_description="Feed a child for a month",
                category="nutrition",
                image_url="/images/nutrition.jpg",
                goal_amount=30000,
                raised_amount=18000,
                beneficiaries_count=200,
                location="Tanzania",
                is_featured=True
            ),
            Program(
                title="Healthcare Initiative",
                slug="healthcare-initiative",
                description="Providing medical care and health education",
                short_description="Support healthcare for communities",
                category="healthcare",
                image_url="/images/healthcare.jpg",
                goal_amount=75000,
                raised_amount=45000,
                beneficiaries_count=500,
                location="Uganda",
                is_featured=False
            )
        ]
        
        for program in programs:
            db.session.add(program)
        
        # Create sample stories
        stories = [
            Story(
                title="Maria's Journey to Success",
                slug="maria-journey-to-success",
                content="Maria was struggling with school until she joined our education program...",
                excerpt="How education changed Maria's life forever",
                beneficiary_name="Maria",
                beneficiary_age=12,
                image_url="/images/maria.jpg",
                program_id=1,
                category="success_story",
                is_featured=True,
                published_at=datetime.utcnow()
            )
        ]
        
        for story in stories:
            db.session.add(story)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)