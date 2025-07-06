# Phishing Detection Using Machine Learning

This is a command-line tool that uses a machine learning model to detect phishing URLs based on handcrafted features. The project is built with Python and structured for clarity, reusability, and extension.

## Features

- URL feature extraction
- ML classifier (Random Forest)
- Detects phishing vs legitimate URLs
- Command-line interface for real-time predictions
- Lightweight and dependency-minimal

## Project Structure

Phishing-Detection/
├── data/ # Dataset storage
├── models/ # Trained ML model
├── src/ # Core logic modules
│ ├── features.py # Feature extraction methods
│ ├── train.py # Model training logic
│ └── utils.py # Dataset loading and preprocessing
├── main.py # Pipeline entry for training
├── predict.py # CLI for URL prediction
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## How It Works

1. `main.py` loads a labeled dataset and extracts meaningful features from each URL.
2. A Random Forest Classifier is trained and saved to `models/phishing_model.joblib`.
3. `predict.py` can be used to test new URLs against the trained model.

## Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Train the model

Make sure your dataset is present at data/phishing_data.csv:

python3 main.py

3. Predict from command-line

python3 predict.py "http://example.com"

Features Extracted

The following features are extracted from the input URL for prediction:

    url_length

    num_dots

    num_slashes

    num_hyphens

    has_ip

    has_at_symbol

    has_https

All feature engineering logic is defined in src/features.py.
Tech Stack

    Python 3.10+

    scikit-learn

    pandas

    joblib

Notes

    Dataset used is a publicly available phishing dataset.

    You can replace the dataset CSV and retrain using the same script.

    CLI is kept minimal for testing and academic demonstration. For production, consider expanding to API or web interface.
