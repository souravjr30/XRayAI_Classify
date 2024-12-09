from tensorflow.keras.models import load_model
from config import Config

class ModelLoader:
    @staticmethod
    def load_model():
        """Load the pre-trained model."""
        try:
            return load_model(Config.MODEL_PATH)
        except Exception as e:
            print(f"Error loading model: {e}")
            return None