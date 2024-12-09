from config import Config

def is_allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    
    Args:
        filename: Name of the file to check
        
    Returns:
        bool: True if file extension is allowed, False otherwise
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS