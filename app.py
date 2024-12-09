from flask import Flask
import os
from routes.main import main
from routes.api import api
from config import Config

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')
    
    # Ensure upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)