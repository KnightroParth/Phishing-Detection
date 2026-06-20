"""
Flask API for real-time phishing URL classification.

Reuses the same model and feature extraction logic as predict.py,
just exposed over HTTP instead of the command line.

Run:
    python3 app.py

Test:
    curl -X POST http://localhost:5000/predict \
        -H "Content-Type: application/json" \
        -d '{"url": "http://example.com"}'
"""

from flask import Flask, request, jsonify
import pandas as pd
import joblib

from src.features import extract_features

app = Flask(__name__)

MODEL_PATH = "models/phishing_model.joblib"

# Load the model once at startup instead of on every request
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    model = None
    print("Model not found. Run `python3 main.py` first to train and save it.")


@app.route("/", methods=["GET"])
def health_check():
    """Simple endpoint to confirm the API is up."""
    return jsonify({"status": "ok", "message": "Phishing Detection API is running"})


@app.route("/predict", methods=["POST"])
def predict():
    """
    Expects JSON body: {"url": "http://example.com"}
    Returns: {"url": ..., "prediction": "phishing" | "legitimate"}
    """
    if model is None:
        return jsonify({"error": "Model not loaded. Run main.py to train it first."}), 503

    data = request.get_json(silent=True)
    if not data or "url" not in data:
        return jsonify({"error": "Request body must be JSON with a 'url' field."}), 400

    url = data["url"]

    try:
        features = extract_features(url)
        X = pd.DataFrame([features])
        prediction = model.predict(X)[0]
        result = "phishing" if prediction == 1 else "legitimate"

        return jsonify({
            "url": url,
            "prediction": result,
            "raw_label": int(prediction)
        })
    except Exception as e:
        return jsonify({"error": f"Failed to process URL: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
