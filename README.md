# 🍅 Tomato Disease Detection System

A comprehensive web application for detecting tomato plant diseases using deep learning, with Kannada voice AI assistant, and profit analysis tools.

## Features

- **Disease Detection**: Upload tomato leaf images to detect 11 different diseases
- **Voice AI Assistant**: Kannada-only voice interface for agriculture queries
- **Profit Analyzer**: Calculate farming profits and costs
- **Government Data**: Access MSP prices and market information

## Supported Diseases

1. Bacterial Spot
2. Early Blight
3. Late Blight
4. Leaf Mold
5. Septoria Leaf Spot
6. Spider Mites (Two-spotted spider mite)
7. Target Spot
8. Tomato Mosaic Virus
9. Tomato Yellow Leaf Curl Virus
10. Powdery Mildew
11. Healthy

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (optional, for cloning)

### Step 1: Clone or Download

```bash
git clone https://github.com/YOUR_USERNAME/TomatoDisease.git
cd TomatoDisease
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies include:**
- Flask (Web framework)
- TensorFlow (Deep learning)
- Pillow (Image processing)
- NumPy (Numerical operations)
- gTTS (Text-to-speech for Kannada)
- requests, beautifulsoup4 (Web scraping)

### Step 3: Verify Model Files

Ensure the following files exist in `saved_models/`:
- `tomato_disease_model.h5` (Main model)
- `class_indices.json` (Disease class mappings)

## Running the Application

### Start the Flask Server

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000`

### Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage Guide

### 1. Disease Detection

1. Navigate to the home page
2. Click "Choose File" and select a tomato leaf image
3. Click "Predict Disease"
4. View the prediction results with confidence percentage
5. Get treatment recommendations in Kannada

### 2. Voice AI Assistant (Kannada Only)

1. Click "Voice AI" in the navigation menu
2. Click the microphone button
3. Speak your agriculture question in Kannada
4. Listen to the audio response
5. Read the text response

**Example Questions:**
- "ಬ್ಯಾಕ್ಟೀರಿಯಾ ಸ್ಪಾಟ್ ಏನು ಮಾಡಬೇಕು?" (What to do for bacterial spot?)
- "ಟಮಾಟೊ ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಎಷ್ಟು?" (What is tomato market price?)
- "ಸೂಕ್ತ ತಾಪಮಾನ ಎಷ್ಟು?" (What is the suitable temperature?)

### 3. Profit Analyzer

1. Click "Profit Analyser" in the navigation menu
2. Enter your farming details:
   - Land area (acres)
   - Total investment
   - Yield (kg)
   - Selling price per kg
3. Click "Calculate Profit"
4. View detailed profit breakdown

## Project Structure

```
TomatoDisease/
├── app.py                          # Main Flask application
├── voice_assistant_kn.py           # Kannada voice assistant logic
├── government_data.py              # MSP and market data
├── test_model.py                   # Model testing script
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore file
│
├── data/                           # Training dataset
│   └── tomato/
│       ├── Bacterial_spot/
│       ├── Early_blight/
│       ├── healthy/
│       └── ... (other disease folders)
│
├── saved_models/                   # Trained model files
│   ├── tomato_disease_model.h5
│   ├── class_indices.json
│   └── training_history.json
│
├── static/                         # Static files
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   ├── audio/                      # Generated TTS audio
│   └── uploads/                    # Uploaded images
│
├── templates/                      # HTML templates
│   ├── index.html                  # Disease detection page
│   ├── result.html                 # Prediction results
│   ├── voice_ai.html               # Voice assistant interface
│   ├── profit_analyser.html        # Profit calculator
│   └── profit_result.html          # Profit results
│
└── training/                       # Model training scripts
    └── train_tomato_model.py
```

## API Endpoints

- `GET /` - Home page (disease detection)
- `POST /predict` - Disease prediction endpoint
- `GET /voice-ai` - Voice AI interface
- `POST /voice-ai/process` - Process voice queries
- `GET /profit-analyser` - Profit calculator page
- `POST /calculate-profit` - Calculate profit

## Technology Stack

- **Backend**: Flask (Python)
- **Deep Learning**: TensorFlow/Keras
- **Voice Recognition**: Web Speech API
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Frontend**: HTML, CSS, JavaScript
- **Image Processing**: Pillow, NumPy

## Voice AI Knowledge Base

The Kannada voice assistant can answer questions about:
- **Diseases**: Treatment for bacterial spot, early blight, late blight, etc.
- **Farming**: Sowing time, harvest, spacing, varieties
- **Market**: Prices, costs, profit margins, subsidies
- **Weather**: Temperature requirements, rain season management
- **Irrigation**: Drip irrigation, water needs
- **Resources**: Training, insurance, loans, expert advice

## Testing the Model

To test the disease detection model:

```bash
python test_model.py
```

## Training the Model

To retrain the model with your own dataset:

```bash
python training/train_tomato_model.py
```

## Troubleshooting

### Port Already in Use
```bash
# Kill the process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

### Module Not Found Error
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### TensorFlow Issues
```bash
# Install specific TensorFlow version
pip install tensorflow==2.13.0
```

### Audio Not Playing
- Ensure gTTS is installed: `pip install gTTS`
- Check browser permissions for audio playback
- Verify `static/audio/` directory exists

## Browser Requirements

- **Recommended**: Google Chrome, Microsoft Edge
- **Voice Recognition**: Requires microphone access
- **Audio Playback**: HTML5 audio support

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available for educational purposes.

## Support

For issues or questions:
- Create an issue on GitHub
- Contact the development team

## Acknowledgments

- TensorFlow/Keras for deep learning framework
- PlantVillage dataset for training images
- gTTS for Kannada text-to-speech
- Flask framework for web development

---

**Made with ❤️ for Indian farmers**
