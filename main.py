"""
AI-Powered Phishing Detection System
Author: KnightroParth
Description:
    A CLI-based tool that extracts handcrafted features from URLs,
    trains a machine learning model, evaluates it, and saves the trained model
    for use in phishing detection applications.

    This script uses a labeled dataset of URLs and applies classic feature engineering
    + ML classification (Random Forest).
"""
"""
Main script to run phishing detection pipeline.
"""

from src.utils import load_dataset
from src.train import train_and_save_model
import os
import sys

if __name__ == "__main__":
    print(" Starting phishing detection pipeline...\n")

    # Check if dataset exists
    dataset_path = "data/phishing_data.csv"
    if not os.path.exists(dataset_path):
        print(f" Dataset not found at {dataset_path}")
        sys.exit(1)

    # Step 1: Load dataset and extract features
    X, y = load_dataset(dataset_path)

    # Step 2: Train model and save to file
    train_and_save_model(X, y, model_path="models/phishing_model.joblib")

    print("\n Pipeline complete.")

