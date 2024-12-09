# X-Ray Intensity Classifier

A Flask-based web application that uses deep learning to classify X-ray images based on their intensity levels. This project demonstrates the implementation of a medical imaging AI system using modern web technologies and machine learning.

## Features

- Upload and classify X-ray images
- Real-time image processing and analysis
- Intensity classification into four categories: Normal, Mild, Moderate, and Severe
- Confidence score for each prediction
- Modern, responsive web interface
- Secure file handling and validation

## Technical Stack

- **Backend**: Flask (Python)
- **Machine Learning**: TensorFlow/Keras
- **Image Processing**: OpenCV
- **Frontend**: HTML5, TailwindCSS, JavaScript
- **Data Handling**: NumPy, Pillow

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/xray-classifier.git
cd xray-classifier
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
├── app.py                 # Application factory
├── config.py             # Configuration
├── requirements.txt      # Python dependencies
├── routes/
│   ├── main.py          # Main routes
│   └── api.py           # API routes
├── services/
│   ├── image_processing/
│   │   ├── enhancer.py  # Image enhancement
│   │   └── preprocessor.py # Image preprocessing
│   └── ml/
│       ├── model_loader.py # Model loading
│       └── predictor.py    # Prediction logic
├── utils/
│   └── file_validator.py # File validation
└── templates/
    └── index.html       # Web interface
```

## Usage

1. Open the web interface in your browser
2. Upload an X-ray image using the file upload button
3. Click "Analyze X-Ray" to process the image
4. View the classification results and confidence score

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.