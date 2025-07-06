"""
Model training logic for phishing detection.
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from .evaluate import evaluate_model

def train_and_save_model(X, y, model_path='models/phishing_model.joblib'):
    """
    Trains a model and saves it to disk.

    Parameters:
        X (DataFrame): Features
        y (Series): Labels
        model_path (str): Path to save model

    Returns:
        model: Trained classifier
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    evaluate_model(model, X_test, y_test)
    joblib.dump(model, model_path)
    print(f"\n Model saved to: {model_path}")

    return model

