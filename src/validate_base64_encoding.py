import base64
import os

def encode_image_to_base64(image_path):
    """
    Encodes an image to a Base64 string.
    :param image_path: Path to the image file.
    :return: Base64 string of the image.
    """
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return encoded_string
    except Exception as e:
        print(f"Error encoding image {image_path} to Base64: {e}")
        return None

if __name__ == "__main__":
    image_path = "/workspaces/marketplace_listing/new_folder/product_1/test_image.jpg"
    encoded_image = encode_image_to_base64(image_path)

    if encoded_image:
        print("Base64 Encoding Successful")
        print(encoded_image[:100])  # Print the first 100 characters to verify
    else:
        print("Base64 Encoding Failed")
