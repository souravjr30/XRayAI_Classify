import cv2
import numpy as np
from config import Config
from .enhancer import ImageEnhancer

class ImagePreprocessor:
    def __init__(self):
        """Initialize the image preprocessor with configuration."""
        self.target_size = Config.TARGET_SIZE
        self.enhancer = ImageEnhancer()
    
    def preprocess(self, image_path):
        """
        Preprocess the X-ray image for classification.
        
        Args:
            image_path: Path to the input image
            
        Returns:
            numpy.ndarray: Preprocessed image ready for classification
        """
        # Read image
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        # Enhance contrast
        image = self.enhancer.enhance_contrast(image)
        
        # Resize
        image = cv2.resize(image, self.target_size)
        
        # Normalize pixel values
        image = image / 255.0
        
        # Add channel dimension
        image = np.expand_dims(image, axis=-1)
        
        return image