"""
URL-based feature extraction for the phishing detection model.

All features are computed directly from the URL string and its parsed
components (scheme, hostname, path, query) — no live network requests
or page content needed, keeping this lightweight and dependency-minimal.
"""

import re
import math
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = [
    "login", "verify", "secure", "account", "update",
    "confirm", "bank", "signin", "webscr", "paypal",
]

IP_PATTERN = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")


def _shannon_entropy(s: str) -> float:
    """How 'random' a string looks. Phishing URLs often score higher
    than legitimate ones due to randomized subdomains or paths."""
    if not s:
        return 0.0
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    length = len(s)
    return -sum((count / length) * math.log2(count / length) for count in freq.values())


def extract_features(url: str) -> dict:
    parsed = urlparse(url if "://" in url else f"http://{url}")
    hostname = parsed.hostname or ""
    path = parsed.path or ""
    query = parsed.query or ""
    domain_parts = hostname.split(".") if hostname else []
    tld = domain_parts[-1] if domain_parts else ""

    return {
        # Structural / length-based
        "url_length": len(url),
        "hostname_length": len(hostname),
        "path_length": len(path),
        "tld_length": len(tld),

        # Character counts
        "num_dots": url.count("."),
        "num_hyphens": url.count("-"),
        "num_underscores": url.count("_"),
        "num_slashes": url.count("/"),
        "num_digits": sum(c.isdigit() for c in url),
        "num_letters": sum(c.isalpha() for c in url),
        "num_special_chars": sum(not c.isalnum() and c not in "./:-_" for c in url),
        "num_equal_signs": url.count("="),
        "num_percent_signs": url.count("%"),
        "num_at_symbols": url.count("@"),

        # Structural flags
        "num_subdomains": max(len(domain_parts) - 2, 0),
        "num_query_params": query.count("&") + 1 if query else 0,
        "has_ip_address": bool(IP_PATTERN.match(hostname)),
        "has_https_scheme": parsed.scheme == "https",
        "has_port": bool(parsed.port),
        "has_double_slash_redirect": url.find("//", 7) != -1,

        # Content-based heuristic
        "has_suspicious_keyword": any(word in url.lower() for word in SUSPICIOUS_KEYWORDS),

        # Randomness measure
        "url_entropy": round(_shannon_entropy(url), 3),
    }
