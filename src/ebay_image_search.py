import os
import base64
import requests
from utils.logger import get_logger

logger = get_logger(__name__)

def encode_image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        logger.error(f"Error encoding image {image_path} to Base64: {e}")
        return None

def search_image_on_ebay(encoded_image, oauth_token):
    ebay_search_url = "https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search_by_image"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {oauth_token}"
    }
    payload = {
        "image": encoded_image
    }

    try:
        response = requests.post(ebay_search_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error searching image on eBay: {e}")
        return None

if __name__ == "__main__":
    image_path = "/workspaces/marketplace_listing/new_folder/product_1/test_image.jpg"
    
    # Read the OAuth token from the file
    with open('oauth_token.txt', 'r') as token_file:
        oauth_token = token_file.read().strip()
    
    encoded_image = encode_image_to_base64(image_path)
    if encoded_image:
        search_results = search_image_on_ebay(encoded_image, oauth_token)
        if search_results:
            logger.info(f"Search results for image {image_path}: {search_results}")
