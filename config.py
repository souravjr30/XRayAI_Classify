class Config:
    """Application configuration."""
    # Flask configuration
    SECRET_KEY = 'your-secret-key-here'  # Change this in production
    
    # File upload configuration
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Model configuration
    MODEL_PATH = 'models/xray_classifier.h5'
    TARGET_SIZE = (224, 224)  # Input size for the model
    INTENSITY_CLASSES = ['Normal', 'Mild', 'Moderate', 'Severe']