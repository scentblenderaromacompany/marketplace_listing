import os
import shutil
import uuid
from datetime import datetime
import sqlite3
from utils.logger import get_logger

logger = get_logger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEW_FOLDER_DIR = os.path.join(BASE_DIR, 'new_folder')
PROCESSED_FOLDER_DIR = os.path.join(BASE_DIR, 'processed')
DB_PATH = os.path.join(BASE_DIR, 'data', 'sku_tracking.db')

def setup_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sku_tracking (
            id INTEGER PRIMARY KEY,
            folder_name TEXT,
            sku TEXT
        )
    ''')
    conn.commit()
    conn.close()

def generate_sku(prefix='', suffix=''):
    return f"{prefix}{uuid.uuid4().hex[:8]}{suffix}"

def process_folders():
    setup_database()
    
    processed_count = 0
    start_sku = None
    end_sku = None
    
    for folder_name in os.listdir(NEW_FOLDER_DIR):
        folder_path = os.path.join(NEW_FOLDER_DIR, folder_name)
        if os.path.isdir(folder_path):
            sku = generate_sku(prefix='SKU_', suffix='')
            new_folder_name = sku
            new_folder_path = os.path.join(PROCESSED_FOLDER_DIR, new_folder_name)
            shutil.move(folder_path, new_folder_path)
            
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO sku_tracking (folder_name, sku) VALUES (?, ?)', (new_folder_name, sku))
            conn.commit()
            conn.close()
            
            if not start_sku:
                start_sku = sku
            end_sku = sku
            
            processed_count += 1
    
    if processed_count > 0:
        timestamp = datetime.now().strftime('%m-%d-%Y_%I-%M_%p')
        processed_folder_name = f"{timestamp}_Processed_{start_sku}-{end_sku}_Total_{processed_count}"
        os.rename(PROCESSED_FOLDER_DIR, os.path.join(BASE_DIR, processed_folder_name))
        
        os.makedirs(PROCESSED_FOLDER_DIR)  # Recreate processed directory for next batch
    
    logger.info(f"Processed {processed_count} folders. New folder: {processed_folder_name}")

if __name__ == "__main__":
    process_folders()
