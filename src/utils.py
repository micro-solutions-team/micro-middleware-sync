import time
import logging
import functools
from datetime import datetime

def retry_request(retries=3, delay=2):
    """
    A decorator to retry a function if it fails. 
    Crucial for unstable corporate internal networks.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logging.warning(f"⚠️ Attempt {attempt+1} failed. Retrying in {delay}s...")
                    time.sleep(delay)
            logging.error(f"❌ All {retries} attempts failed.")
            return False
        return wrapper
    return decorator

def format_corporate_name(name):
    """Standardizes ALL CAPS legacy names to Title Case."""
    return name.strip().title() if name else "Unknown"

def validate_record(record):
    """Ensures we don't send garbage data to the API."""
    if not record.get('id'):
        return False, "Missing ID"
    return True, "Valid"