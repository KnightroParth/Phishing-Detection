"""
Utility functions: loading data, label mapping, etc.
"""

import pandas as pd
from .features import extract_features

def load_dataset(path):
    """
    Loads the dataset and applies feature extraction.

    Parameters:
        path (str): Path to the CSV file.

    Returns:
        tuple: X (features), y (labels)
    """

    # Load dataset safely
    df = pd.read_csv(path, encoding='latin1', on_bad_lines='skip')

    # Rename 'domain' column to 'url' for compatibility
    if 'domain' in df.columns:
        df.rename(columns={'domain': 'url'}, inplace=True)

    # Validate required columns
    if 'url' not in df.columns or 'label' not in df.columns:
        raise ValueError("CSV must contain 'url' and 'label' columns.")

    # Extract features from each URL
    features = df['url'].apply(extract_features).apply(pd.Series)

    # Encode labels (phishing = 1, safe = 0)
    labels = df['label'].apply(lambda x: 1 if str(x).lower() == 'phishing' else 0)

    return features, labels
