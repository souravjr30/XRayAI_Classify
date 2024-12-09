from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from services.image_processing.preprocessor import ImagePreprocessor
from services.ml.predictor import XRayPredictor
from utils.file_validator import is_allowed_file
from config import Config

api = Blueprint('api', __name__)

# Initialize services
predictor = XRayPredictor()
preprocessor = ImagePreprocessor()

@api.route('/classify', methods=['POST'])
def classify_xray():
    """Handle X-ray image classification requests."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and is_allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        try:
            # Process the image
            processed_image = preprocessor.preprocess(filepath)
            
            # Get classification
            intensity, confidence = predictor.predict(processed_image)
            
            return jsonify({
                'intensity': intensity,
                'confidence': float(confidence),
                'message': f'Image classified as {intensity} intensity with {confidence:.2f}% confidence'
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            # Clean up
            if os.path.exists(filepath):
                os.remove(filepath)
    
    return jsonify({'error': 'Invalid file type'}), 400