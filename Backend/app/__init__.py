from flask import Flask
from app.config import config
from app.extensions import db, migrate, mail, cors, ma
import os

def create_app(config_name=None):
    """Application factory pattern"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": app.config['CORS_ORIGINS']}})
    ma.init_app(app)
    
    # Register blueprints
    from app.routes import donations, programs, stories, newsletter, volunteers, contact
    
    app.register_blueprint(donations.bp, url_prefix='/api/donations')
    app.register_blueprint(programs.bp, url_prefix='/api/programs')
    app.register_blueprint(stories.bp, url_prefix='/api/stories')
    app.register_blueprint(newsletter.bp, url_prefix='/api/newsletter')
    app.register_blueprint(volunteers.bp, url_prefix='/api/volunteers')
    app.register_blueprint(contact.bp, url_prefix='/api/contact')
    
    # Health check endpoint
    @app.route('/api/health')
    def health_check():
        return {'status': 'healthy'}, 200
    
    return app