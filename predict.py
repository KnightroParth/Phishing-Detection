"""
CLI tool to predict whether a URL is phishing or safe.
Usage:
    python3 predict.py "http://example.com"
"""

import pandas as pd
import sys
import joblib
from src.features import extract_features

MODEL_PATH = "models/phishing_model.joblib"

def predict_url(url):
    try:
        model = joblib.load(MODEL_PATH)
    except FileNotFoundError:
        print("❌ Model not found. Please run `main.py` to train and save the model.")
        return

    # Extract features from input URL
    features = extract_features(url)
    X = pd.DataFrame([features])

    prediction = model.predict(X)[0]
    print("\n🔍 URL:", url)
    if prediction == 1:
        print("❌ Prediction: Phishing site")
    else:
        print("✅ Prediction: Legitimate site")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:\n  python3 predict.py \"http://suspicious-site.com\"")
        sys.exit(1)

    input_url = sys.argv[1]
    predict_url(input_url)

