import os
import json
import random
import tempfile
from pathlib import Path
from datetime import datetime

import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image

from flask import Flask, request, render_template, redirect, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename

# Import modules
from government_data import calculate_with_government_data
from voice_assistant_kn import get_agriculture_response, LANGUAGE

# Import speech libraries
try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False
    print("Warning: gTTS not installed. Text-to-speech will not work.")


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "saved_models" / "tomato_disease_model.h5"
CLASS_IND_PATH = BASE_DIR / "saved_models" / "class_indices.json"
DATA_DIR = BASE_DIR / "data" / "tomato"
UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"
AUDIO_FOLDER = BASE_DIR / "static" / "audio"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = str(UPLOAD_FOLDER)


# Custom Jinja2 filter for number formatting
@app.template_filter('number_format')
def number_format(value):
    """Format number with commas for thousands"""
    try:
        return "{:,.0f}".format(float(value))
    except (ValueError, TypeError):
        return value


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Load model at startup (fail early if missing)
model = None
labels = None
mapping_source = None
try:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found at: {MODEL_PATH}")

    model = tf.keras.models.load_model(str(MODEL_PATH))

    # Try to load saved class_indices mapping
    if CLASS_IND_PATH.exists():
        with open(CLASS_IND_PATH, "r", encoding="utf-8") as fh:
            class_indices = json.load(fh)
        # invert mapping to list by index
        labels = [None] * len(class_indices)
        for name, idx in class_indices.items():
            labels[idx] = name
        mapping_source = "saved_models/class_indices.json"
    else:
        # Fallback: infer classes from data folder (alphabetical, same order as Keras flow_from_directory)
        if DATA_DIR.exists():
            folders = [d.name for d in sorted(DATA_DIR.iterdir()) if d.is_dir()]
            labels = folders
            mapping_source = "data/tomato (inferred, alphabetical)"
        else:
            labels = None
            mapping_source = "none"
except Exception as e:
    # Keep model None and surface error on pages
    model = None
    labels = None
    mapping_source = f"error: {e}"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", model_ready=(model is not None), mapping_source=mapping_source)


@app.route("/profit-analyser", methods=["GET"])
def profit_analyser():
    return render_template("profit_analyser.html")


@app.route("/voice-ai", methods=["GET"])
def voice_ai():
    return render_template("voice_ai.html")


@app.route("/voice-ai/process", methods=["POST"])
def process_voice():
    """Process voice question and generate response"""
    try:
        data = request.get_json()
        question = data.get("question", "").strip()

        if not question:
            return jsonify({
                "success": False,
                "error": "No question provided"
            })

        # Get agriculture response (Kannada only)
        response = get_agriculture_response(question)

        # Generate audio response using gTTS (Kannada)
        audio_url = None
        if GTTS_AVAILABLE:
            try:
                # Generate TTS in Kannada
                tts = gTTS(text=response, lang='kn', slow=False)
                
                # Save to file with timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                audio_filename = f"response_{timestamp}_kn.mp3"
                audio_path = AUDIO_FOLDER / audio_filename
                tts.save(str(audio_path))
                
                audio_url = f"/static/audio/{audio_filename}"
            except Exception as e:
                print(f"TTS generation error: {e}")
                # Continue without audio if TTS fails

        return jsonify({
            "success": True,
            "response": response,
            "audio_url": audio_url
        })

    except Exception as e:
        print(f"Error processing voice request: {e}")
        return jsonify({
            "success": False,
            "error": str(e)
        })


@app.route("/profit-analyser/analyse", methods=["POST"])
def analyse_profit():
    # Get form data
    crop_type = request.form.get("crop_type")
    season = request.form.get("season")
    land_size = float(request.form.get("land_size"))
    num_plants = int(request.form.get("num_plants"))
    farming_type = request.form.get("farming_type")
    organic = request.form.get("organic")

    # Prepare data dict
    data = {
        "crop_type": crop_type,
        "season": season,
        "land_size": land_size,
        "num_plants": num_plants,
        "farming_type": farming_type,
        "organic": organic
    }

    # Perform analysis using government data
    analysis = calculate_with_government_data(data)

    return render_template("profit_result.html", data=data, analysis=analysis)


@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return render_template("index.html", model_ready=False, mapping_source=mapping_source, error="Model not loaded")

    if "file" not in request.files:
        return redirect(url_for("index"))
    file = request.files["file"]
    if file.filename == "":
        return redirect(url_for("index"))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = UPLOAD_FOLDER / filename
        file.save(str(save_path))

        # Preprocess image
        img = image.load_img(str(save_path), target_size=(224, 224))
        x = image.img_to_array(img) / 255.0
        x = np.expand_dims(x, axis=0)

        preds = model.predict(x)
        preds = preds[0]
        top_idx = int(np.argmax(preds))
        top_prob = float(preds[top_idx])

        if labels and top_idx < len(labels):
            predicted_label = labels[top_idx]
        else:
            predicted_label = str(top_idx)

        # Compute probabilities list (label, prob)
        prob_list = []
        if labels and len(labels) == len(preds):
            for i, p in enumerate(preds):
                prob_list.append((labels[i], float(p)))
        else:
            for i, p in enumerate(preds):
                prob_list.append((str(i), float(p)))

        prob_list = sorted(prob_list, key=lambda x: x[1], reverse=True)

        # Define affected rate: if predicted label is 'healthy' -> 0, else top_prob*100
        if predicted_label.lower().startswith("healthy"):
            affected_rate = 0.0
        else:
            affected_rate = top_prob * 100.0

        return render_template(
            "result.html",
            image_url=f"uploads/{filename}",
            predicted_label=predicted_label,
            confidence=top_prob * 100.0,
            affected_rate=affected_rate,
            prob_list=prob_list,
            mapping_source=mapping_source,
        )

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
