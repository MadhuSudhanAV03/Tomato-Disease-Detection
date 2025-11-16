# 🚀 Quick Start Guide - Krishi Voice Assistant

## Prerequisites
- Python 3.8 or higher
- Modern web browser (Chrome or Edge recommended)
- Microphone access

## Installation Steps

### 1. Install Dependencies
```bash
cd m:\TomatoDisease
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- TensorFlow (disease detection model)
- Pillow, NumPy (image processing)
- requests, beautifulsoup4 (government data)
- gTTS (text-to-speech)
- SpeechRecognition (voice input)

### 2. Verify Installation
```bash
# Test the voice assistant module
python test_voice_assistant.py
```

Expected output: Tests for all 5 languages with responses

### 3. Start the Application
```bash
python app.py
```

Expected output:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

### 4. Access Voice AI
Open your browser and navigate to:
```
http://localhost:5000/voice-ai
```

## First-Time Setup

### Allow Microphone Access
1. When you first click the microphone button, your browser will ask for permission
2. Click **Allow** to grant microphone access
3. The permission is saved for future visits

### Select Your Language
1. Click on one of the 5 language buttons:
   - English
   - ಕನ್ನಡ (Kannada)
   - हिंदी (Hindi)
   - తెలుగు (Telugu)
   - தமிழ் (Tamil)

2. The selected language will be highlighted in green

### Ask a Question
1. Click the large green microphone button
2. It will turn red and pulse - this means it's listening
3. Speak your agriculture question clearly
4. The microphone will automatically stop after you finish speaking
5. Your question will appear in the "Your Question" box
6. The AI response will appear in the "AI Response" box
7. Audio will automatically play (you can replay using the audio player)

## Sample Questions to Try

### English
- "What causes early blight in tomatoes?"
- "How to improve soil health?"
- "What is the market price for tomatoes?"
- "Tell me about drip irrigation"

### Kannada (ಕನ್ನಡ)
- "ಟೊಮೇಟೊ ರೋಗಗಳು ಯಾವುವು?"
- "ಮಣ್ಣಿನ ಆರೋಗ್ಯ ಸುಧಾರಿಸುವುದು ಹೇಗೆ?"
- "ಟೊಮೇಟೊ ಬೆಲೆ ಏನು?"

### Hindi (हिंदी)
- "टमाटर की फसल के लिए कौन सा उर्वरक सबसे अच्छा है?"
- "मिट्टी का पीएच कैसे सुधारें?"
- "टमाटर की कीमत क्या है?"

## Troubleshooting

### Problem: Microphone button doesn't respond
**Solution**: 
- Check browser compatibility (use Chrome or Edge)
- Ensure microphone is connected and working
- Grant microphone permissions in browser settings

### Problem: "Speech recognition is not supported"
**Solution**:
- Switch to Google Chrome or Microsoft Edge
- Firefox doesn't support Web Speech API

### Problem: No audio response
**Solution**:
- Check internet connection (gTTS requires internet)
- Verify gTTS is installed: `pip install gTTS`
- Check browser audio settings

### Problem: Wrong language recognized
**Solution**:
- Ensure correct language is selected before speaking
- Speak clearly and at moderate pace
- Reduce background noise

### Problem: Response says "I can only help with agriculture"
**Solution**:
- This is intentional - the AI only answers agriculture questions
- Try asking about crops, diseases, soil, irrigation, or market

## Navigation

### Access Other Modules
Use the navbar at the top:
- **Disease Prediction**: Upload tomato leaf images for disease detection
- **Profit Analyser**: Calculate farming profitability with government data
- **Voice AI**: Current page - voice-based Q&A

## Tips for Best Results

### Voice Recognition
1. **Speak clearly** - Enunciate words properly
2. **Moderate pace** - Not too fast, not too slow
3. **Quiet environment** - Reduce background noise
4. **Close to microphone** - 6-12 inches distance ideal
5. **Natural pauses** - Brief pause after clicking microphone

### Question Formulation
1. **Be specific**: "What causes early blight?" instead of "Disease problem"
2. **Use keywords**: Include words like crop, disease, soil, price, farming
3. **One topic**: Ask one question at a time
4. **Natural language**: Speak as you would to a person

### Example Good Questions
✅ "How do I treat bacterial spot in tomatoes?"  
✅ "What fertilizer should I use for tomato plants?"  
✅ "When is the best time to plant tomatoes?"

### Example Poor Questions
❌ "Computer repair" (not agriculture)  
❌ "Tell me everything" (too broad)  
❌ "Problem" (not specific enough)

## Advanced Usage

### Interactive Testing Mode
For testing without browser:
```bash
python test_voice_assistant.py --interactive
```

This allows you to:
- Type questions instead of speaking
- Test all languages
- See raw responses without UI

### Automated Testing
Run the full test suite:
```bash
python test_voice_assistant.py
```

This tests:
- All 5 languages
- Disease queries
- Farming tips
- Market information
- Soil management
- Non-agriculture filtering

## Technical Details

### How It Works
1. **Browser captures speech** → Web Speech API
2. **Speech converted to text** → Automatic transcription
3. **Text sent to Flask backend** → `/voice-ai/process` endpoint
4. **AI analyzes question** → Agriculture validation + keyword matching
5. **Response generated** → From knowledge base
6. **Text-to-speech creates audio** → Google TTS (gTTS)
7. **Response returned** → JSON with text + audio URL
8. **Browser displays and plays** → UI updates automatically

### Data Flow
```
User Speech → Browser (Web Speech API) → Text Transcript
                                            ↓
                                    Flask Backend
                                            ↓
                              Voice Assistant Module
                                            ↓
                              ← JSON Response ←
                                            ↓
                              Audio File (gTTS)
                                            ↓
                              Browser Audio Player
```

## System Requirements

### Minimum
- **RAM**: 2 GB
- **Storage**: 500 MB (for model + dependencies)
- **Browser**: Chrome 25+ or Edge 79+
- **Internet**: Required for gTTS

### Recommended
- **RAM**: 4 GB+
- **Storage**: 1 GB
- **Browser**: Latest Chrome or Edge
- **Internet**: Broadband (for faster audio generation)

## File Locations

### Generated Audio Files
```
m:\TomatoDisease\static\audio\
```

Files are named: `response_YYYYMMDD_HHMMSS_lang.mp3`

Example: `response_20240115_143022_en.mp3`

**Cleanup Recommendation**: Delete files older than 24 hours to save space

### Logs
Check Flask console output for errors:
```
TTS generation error: ...
Error processing voice request: ...
```

## Support

### Documentation
- **Comprehensive Guide**: `VOICE_AI_README.md`
- **Implementation Details**: `VOICE_AI_IMPLEMENTATION.md`
- **Source Code**: `voice_assistant.py`, `app.py`

### Common Issues
See "Troubleshooting" section in `VOICE_AI_README.md`

### Testing
Run tests before reporting issues:
```bash
python test_voice_assistant.py
```

## Next Steps

### Explore Other Features
1. **Disease Prediction**: Upload a leaf image → Get disease diagnosis
2. **Profit Analyser**: Input farm details → Get profitability analysis

### Customize
- Add more languages (edit `voice_assistant.py`)
- Expand knowledge base (update `AGRICULTURE_KB`)
- Modify UI theme (edit `templates/voice_ai.html`)

## Quick Reference Card

| Action | Steps |
|--------|-------|
| **Start App** | `python app.py` |
| **Access Voice AI** | `http://localhost:5000/voice-ai` |
| **Select Language** | Click language button |
| **Ask Question** | Click mic → Speak → Wait for response |
| **Replay Audio** | Use audio player controls |
| **Test Without Browser** | `python test_voice_assistant.py --interactive` |
| **View Logs** | Check terminal running `python app.py` |

## Browser Shortcuts

- **Allow Mic**: Click "Allow" when browser asks
- **Reload Page**: `Ctrl + R` (or `Cmd + R` on Mac)
- **Open Console**: `F12` → Console tab (for debugging)
- **Clear Cache**: `Ctrl + Shift + Delete`

---

**Happy Farming! 🌾🎙️**

For detailed documentation, see `VOICE_AI_README.md`
