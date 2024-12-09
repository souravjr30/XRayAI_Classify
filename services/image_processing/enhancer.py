import cv2

class ImageEnhancer:
    @staticmethod
    def enhance_contrast(image):
        """
        Enhance image contrast using CLAHE
        (Contrast Limited Adaptive Histogram Equalization).
        
        Args:
            image: Input image array
            
        Returns:
            numpy.ndarray: Contrast-enhanced image
        """
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        return clahe.apply(image)