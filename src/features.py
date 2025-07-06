"""
Feature extraction logic for phishing detection.
"""

import re
from urllib.parse import urlparse
from collections import OrderedDict

def extract_features(url):

    """
    Extracts handcrafted features from a URL string.

    Parameters:
        url (str): The URL to extract features from.

    Returns:
        dict: Dictionary of extracted features.
    """
    features = OrderedDict()
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['num_slashes'] = url.count('/')
    features['num_hyphens'] = url.count('-')
    features['has_ip'] = 1 if re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url) else 0
    features['has_at_symbol'] = 1 if '@' in url else 0
    features['has_https'] = 1 if urlparse(url).scheme == 'https' else 0
    return features
