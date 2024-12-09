import numpy as np
from config import Config
from .model_loader import ModelLoader

class XRayPredictor:
    def __init__(self):
        """Initialize the X-Ray predictor with a pre-trained model."""
        self.model = ModelLoader.load_model()
        self.classes = Config.INTENSITY_CLASSES
    
    def predict(self, processed_image):
        """
        Predict the intensity class of an X-ray image.
        
        Args:
            processed_image: Preprocessed numpy array of shape (224, 224, 1)
            
        Returns:
            tuple: (predicted_class, confidence_score)
        """
        if self.model is None:
            return self._dummy_predict()
            
        # Add batch dimension
        image_batch = np.expand_dims(processed_image, axis=0)
        
        # Get predictions
        predictions = self.model.predict(image_batch)
        class_idx = np.argmax(predictions[0])
        confidence = predictions[0][class_idx] * 100
        
        return self.classes[class_idx], confidence
    
    def _dummy_predict(self):
        """Dummy prediction for demonstration purposes."""
        import random
        class_idx = random.randint(0, len(self.classes) - 1)
        confidence = random.uniform(70, 99)
        return self.classes[class_idx], confidence