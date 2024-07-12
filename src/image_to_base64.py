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

def save_base64_string(base64_string, output_path):
    """
    Saves a Base64 string to a file.
    :param base64_string: Base64 string of the image.
    :param output_path: Path to save the Base64 string.
    """
    try:
        with open(output_path, "w") as output_file:
            output_file.write(base64_string)
        print(f"Base64 string saved to {output_path}")
    except Exception as e:
        print(f"Error saving Base64 string to {output_path}: {e}")

if __name__ == "__main__":
    image_path = "/workspaces/marketplace_listing/new_folder/product_1/test_image.jpg"
    output_path = "/workspaces/marketplace_listing/new_folder/product_1/test_image_base64.txt"

    print(f"Checking if image file exists: {image_path}")
    if os.path.isfile(image_path):
        print(f"Image file found: {image_path}")
        base64_string = encode_image_to_base64(image_path)
        if base64_string:
            save_base64_string(base64_string, output_path)
    else:
        print(f"Image file not found: {image_path}")
