import sqlite3
import pandas as pd
import requests
import logging
import os
from dotenv import load_dotenv
from utils import retry_request, format_corporate_name, validate_record

# Load environment variables
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
    handlers=[logging.FileHandler("logs/sync.log"), logging.StreamHandler()]
)

@retry_request(retries=int(os.getenv('MAX_RETRIES', 3)), delay=int(os.getenv('RETRY_DELAY', 2)))
def push_to_modern_system(payload):
    """Sends the data with built-in retry logic."""
    response = requests.post(os.getenv('API_ENDPOINT'), json=payload, timeout=5)
    response.raise_for_status() # Triggers the retry if status is 4xx or 5xx
    return True

def run_sync():
    logging.info("--- Starting Enhanced Sync Job ---")
    
    try:
        conn = sqlite3.connect(os.getenv('DB_PATH'))
        df = pd.read_sql_query("SELECT * FROM T_CUSTOMERS_STG", conn)
        conn.close()
    except Exception as e:
        logging.error(f"Database Connection Error: {e}")
        return

    stats = {"success": 0, "failed": 0, "skipped": 0}

    for _, row in df.iterrows():
        # 1. Clean / Transform
        clean_data = {
            "id": row['CUST_ID'],
            "name": format_corporate_name(row['FULL_NAME']),
            "is_active": True if row['STATUS_CODE'] == 'A' else False
        }

        # 2. Validate
        is_valid, reason = validate_record(clean_data)
        if not is_valid:
            logging.warning(f"Skipping Record {row['CUST_ID']}: {reason}")
            stats["skipped"] += 1
            continue

        # 3. Sync
        if push_to_modern_system(clean_data):
            logging.info(f"Synced: {clean_data['name']}")
            stats["success"] += 1
        else:
            stats["failed"] += 1

    logging.info(f"--- Job Finished | Success: {stats['success']} | Failed: {stats['failed']} | Skipped: {stats['skipped']} ---")

if __name__ == "__main__":
    run_sync()