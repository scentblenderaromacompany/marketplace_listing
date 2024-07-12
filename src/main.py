import os
from generate_and_save_oauth_token import generate_and_save_oauth_token
from ebay_image_search import search_image_on_ebay
from folder_processing import process_folders
from train_image_search_bot import train_image_search_model
from train_text_extraction_bot import train_text_extraction_model
from train_price_prediction_bot import train_price_prediction_model
from database_management import update_database

def main():
    # Generate and save OAuth token
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
    generate_and_save_oauth_token(client_id, client_secret)
    
    # Process folders and images
    base_dir = "new_folder"
    oauth_token_path = "oauth_token.txt"
    with open(oauth_token_path, 'r') as token_file:
        oauth_token = token_file.read().strip()
    process_folders(base_dir, oauth_token)
    
    # Train bots
    train_data_dir = "train_data"
    train_image_search_model(train_data_dir, "models/image_search_model.h5")
    train_text_extraction_model(train_data_dir)
    train_price_prediction_model(os.path.join(train_data_dir, "price_data.csv"), "models/price_prediction_model.h5")
    
    # Update database
    update_database("data/sku_tracking.db")

if __name__ == "__main__":
    main()
