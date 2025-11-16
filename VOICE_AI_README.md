# Krishi Voice Assistant - Multilingual Agriculture AI

## Overview
The Krishi Voice Assistant is an intelligent, multilingual voice-based question-answering system designed specifically for farmers. It provides agriculture-only responses in 5 Indian languages, helping farmers get instant advice on crops, diseases, farming practices, and market information.

## Features

### 🌐 Multilingual Support
- **English** - Full support
- **ಕನ್ನಡ (Kannada)** - Complete agricultural knowledge base
- **हिंदी (Hindi)** - Comprehensive farming guidance
- **తెలుగు (Telugu)** - Agricultural advisory in Telugu
- **தமிழ் (Tamil)** - Tamil language farming assistance

### 🎙️ Voice Interaction
- **Speech-to-Text**: Uses browser Web Speech API for voice recognition
- **Text-to-Speech**: Powered by Google Text-to-Speech (gTTS)
- **Real-time Processing**: Instant response generation
- **Audio Playback**: Listen to responses in selected language

### 🌾 Agriculture-Only Responses
The assistant uses intelligent filtering to ensure all responses are agriculture-related:
- Crop diseases and treatment
- Farming techniques and best practices
- Soil management and fertilization
- Irrigation methods
- Market prices and government schemes
- Pest and disease control

## Technical Architecture

### Frontend Components
1. **Language Selector**: 5-button interface for language selection
2. **Voice Interface**: 
   - Large circular microphone button with pulse animation when recording
   - Real-time status indicators
   - Visual feedback for recording state
3. **Transcript Display**: Shows user's spoken question
4. **Response Display**: AI-generated agriculture advice
5. **Audio Player**: Plays back text-to-speech response

### Backend Components

#### `voice_assistant.py`
Main module containing:

```python
# Key Functions:
- is_agriculture_related()     # Validates question is agriculture-focused
- get_agriculture_response()   # Generates appropriate response
- get_disease_info()           # Disease-specific guidance
- get_farming_tips()           # General farming advice
- get_market_info()            # Market and pricing information
- get_soil_info()              # Soil health guidance
```

**Language Configurations**:
```python
LANGUAGES = {
    'en': {'name': 'English', 'code': 'en', 'tts_code': 'en', ...},
    'kn': {'name': 'ಕನ್ನಡ (Kannada)', 'code': 'kn', 'tts_code': 'kn', ...},
    # ... other languages
}
```

**Knowledge Base Structure**:
- `AGRICULTURE_KEYWORDS`: Multilingual keyword lists for validation
- `AGRICULTURE_KB`: Comprehensive knowledge base with:
  - Tomato disease information (causes, symptoms, treatment, prevention)
  - General farming tips (soil health, irrigation, organic farming)
  - Market guidance
  - Soil management

#### Flask Routes (`app.py`)

```python
@app.route("/voice-ai", methods=["GET"])
def voice_ai():
    # Serves the voice assistant interface
    
@app.route("/voice-ai/process", methods=["POST"])
def process_voice():
    # Processes voice questions and generates responses
    # Returns JSON with response text and audio URL
```

**Request Format**:
```json
{
    "question": "What causes early blight in tomatoes?",
    "language": "en"
}
```

**Response Format**:
```json
{
    "success": true,
    "response": "For tomato diseases like Early Blight...",
    "audio_url": "/static/audio/response_20240115_143022_en.mp3"
}
```

### Speech Recognition
Uses browser-native Web Speech API:
- **Supported Browsers**: Chrome, Edge, Safari (limited)
- **Language Codes**:
  - English: `en-US`
  - Kannada: `kn-IN`
  - Hindi: `hi-IN`
  - Telugu: `te-IN`
  - Tamil: `ta-IN`

### Text-to-Speech
Powered by gTTS (Google Text-to-Speech):
- Generates MP3 audio files
- Stores in `/static/audio/` directory
- Automatic cleanup (recommended: implement periodic cleanup)

## Usage Instructions

### For Users
1. **Select Language**: Click on your preferred language button
2. **Click Microphone**: Large green button to start recording
3. **Speak Question**: Ask about any agriculture topic
4. **View Response**: Read the text response and listen to audio

### Example Questions

**English**:
- "What causes leaf curl in tomatoes?"
- "How to improve soil health?"
- "What is the market price for tomatoes?"

**Kannada** (ಕನ್ನಡ):
- "ಟೊಮೇಟೊ ಎಲೆ ಸುರುಳಿಗೆ ಕಾರಣ ಏನು?"
- "ಮಣ್ಣಿನ ಆರೋಗ್ಯ ಸುಧಾರಿಸುವುದು ಹೇಗೆ?"

**Hindi** (हिंदी):
- "टमाटर में पत्ती मरोड़ का क्या कारण है?"
- "मिट्टी की सेहत कैसे सुधारें?"

## Installation & Setup

### Prerequisites
```bash
pip install -r requirements.txt
```

Required packages:
- `Flask>=2.0` - Web framework
- `gTTS` - Text-to-speech generation
- `requests` - HTTP requests

### File Structure
```
TomatoDisease/
├── app.py                          # Flask application
├── voice_assistant.py              # Voice AI logic
├── templates/
│   └── voice_ai.html              # Voice interface template
├── static/
│   ├── css/
│   │   └── style.css              # Styling (includes voice UI)
│   └── audio/                     # Generated audio files
└── requirements.txt
```

### Running the Application
```bash
python app.py
```
Access at: `http://localhost:5000/voice-ai`

## Browser Compatibility

### Speech Recognition Support
- ✅ **Chrome/Edge**: Full support (recommended)
- ⚠️ **Firefox**: Not supported (Web Speech API limitation)
- ⚠️ **Safari**: Limited support

### Audio Playback
- ✅ All modern browsers support MP3 playback

## Response Logic

### Question Classification
1. **Disease Queries**: Keywords like "disease", "sick", "spot", "curl"
   - Returns disease-specific information
   - Includes cause, symptoms, treatment, prevention

2. **Farming Tips**: Keywords like "how to", "tip", "advice"
   - General farming guidance
   - Planting schedules, spacing, irrigation

3. **Market Info**: Keywords like "price", "market", "sell"
   - Current price ranges
   - MSP information
   - eNAM registration guidance

4. **Soil Management**: Keywords like "soil", "fertilizer", "compost"
   - Soil testing advice
   - Fertilizer recommendations
   - Organic farming methods

### Out-of-Scope Handling
Non-agriculture questions receive polite rejection in selected language:
- **English**: "Sorry, I can only help with agriculture-related questions..."
- **Kannada**: "ಕ್ಷಮಿಸಿ, ನಾನು ಕೃಷಿ ವಿಷಯಗಳ ಬಗ್ಗೆ ಮಾತ್ರ ಸಹಾಯ ಮಾಡುತ್ತೇನೆ..."

## Knowledge Base Content

### Tomato Diseases Coverage
1. **Early Blight** (Alternaria solani)
   - Fungal disease with concentric ring spots
   - Treatment: Mancozeb/Chlorothalonil
   
2. **Late Blight** (Phytophthora infestans)
   - Water-soaked spots, rapid spread
   - Treatment: Copper-based fungicides

3. **Bacterial Spot** (Xanthomonas)
   - Small dark spots with yellow halo
   - Treatment: Copper bactericides

4. **Leaf Curl Virus** (TYLCV)
   - Whitefly-transmitted virus
   - Management: Vector control, resistant varieties

### General Agriculture Topics
- Soil health and pH management
- Drip irrigation benefits (40-60% water savings)
- Organic farming practices
- Integrated pest management
- Market linkage (eNAM portal)
- Government subsidies

## Customization

### Adding New Languages
1. Update `LANGUAGES` dict in `voice_assistant.py`
2. Add language button in `voice_ai.html`
3. Translate knowledge base entries
4. Add keywords to `AGRICULTURE_KEYWORDS`

### Expanding Knowledge Base
Edit `AGRICULTURE_KB` dictionary:
```python
AGRICULTURE_KB = {
    'new_topic': {
        'en': { 'subtopic': 'information' },
        'kn': { 'subtopic': 'ಮಾಹಿತಿ' },
        # ... other languages
    }
}
```

### Adding New Question Categories
1. Define keyword set
2. Create handler function (e.g., `get_new_category_info()`)
3. Add conditional in `get_agriculture_response()`

## Performance Considerations

### Audio File Management
- Audio files accumulate in `/static/audio/`
- **Recommendation**: Implement cleanup script
```python
# Example cleanup (files older than 24 hours)
import os
import time
from pathlib import Path

AUDIO_FOLDER = Path("static/audio")
MAX_AGE = 24 * 3600  # 24 hours

for file in AUDIO_FOLDER.glob("*.mp3"):
    if time.time() - file.stat().st_mtime > MAX_AGE:
        file.unlink()
```

### Response Time
- Speech recognition: ~1-3 seconds
- Response generation: <100ms
- TTS generation: ~1-2 seconds
- **Total**: ~2-5 seconds for complete interaction

### Caching Opportunities
- Common questions could be cached
- Pre-generated audio for FAQs
- Response templates for faster generation

## Security Considerations

### Input Validation
- Question text is stripped and validated
- Maximum length could be enforced
- XSS protection via template escaping

### File Storage
- Audio files use timestamp-based naming
- Directory is write-protected (should be configured)
- Regular cleanup prevents disk space issues

## Troubleshooting

### Microphone Not Working
1. **Browser Permissions**: Check if microphone access is granted
2. **HTTPS Required**: Web Speech API requires HTTPS in production
3. **Browser Support**: Use Chrome/Edge for best results

### TTS Not Working
- Check if `gTTS` is installed: `pip install gTTS`
- Verify internet connection (gTTS requires Google API)
- Check audio folder permissions

### Wrong Language Recognition
- Ensure correct language is selected before speaking
- Speak clearly and at moderate pace
- Background noise can affect accuracy

## Future Enhancements

### Planned Features
1. **Offline TTS**: Use local TTS engines (e.g., Pyttsx3)
2. **Voice Activity Detection**: Auto-start/stop recording
3. **Conversation Context**: Remember previous questions
4. **Image Integration**: "Show me pictures of early blight"
5. **Location-Based Advice**: Weather-specific recommendations
6. **Expert Connect**: Option to talk to human agronomist

### AI Improvements
1. **LLM Integration**: Use GPT/Claude for more natural responses
2. **RAG System**: Retrieve from larger agricultural databases
3. **Personalization**: User profiles and farming history
4. **Crop Calendars**: Season-specific advice

## Credits & References

### Data Sources
- Disease information: ICAR research publications
- Market data: AGMARKNET, eNAM
- Best practices: State agricultural departments

### Technologies
- **Flask**: Web framework
- **Web Speech API**: Browser speech recognition
- **gTTS**: Google Text-to-Speech
- **TensorFlow**: Disease detection model (integrated)

## License
Part of the TomatoDisease project. See main README for license information.

## Support
For issues or questions:
1. Check browser console for errors
2. Verify microphone permissions
3. Ensure all dependencies are installed
4. Review Flask application logs

---

**Version**: 1.0  
**Last Updated**: 2024  
**Maintainer**: TomatoDisease Project Team
