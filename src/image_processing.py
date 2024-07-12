import os
from PIL import Image, ImageEnhance
import cv2
import numpy as np
from utils.logger import get_logger

logger = get_logger(__name__)

def rotate_image(image):
    if hasattr(image, '_getexif'):
        orientation = 274  # cf. ExifTags
        exif = image._getexif()
        if exif is not None:
            orientation = exif.get(0x112, 1)
            rotate_values = {
                3: 180,
                6: 270,
                8: 90
            }
            if orientation in rotate_values:
                image = image.rotate(rotate_values[orientation], expand=True)
    return image

def center_image(image):
    # Example centering implementation (depends on specific requirements)
    return image

def crop_image(image):
    image_array = np.array(image)
    gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 30, 100)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        x, y, w, h = cv2.boundingRect(contours[0])
        image_array = image_array[y:y+h, x:x+w]
    
    return Image.fromarray(image_array)

def enhance_image(image):
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.2)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.2)

    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(1.2)
    
    return image

def process_image(image_path):
    try:
        image = Image.open(image_path)
        image = rotate_image(image)
        image = center_image(image)
        image = crop_image(image)
        image = enhance_image(image)
        image = image.convert("RGB")
        
        # Convert to PNG
        base_name = os.path.basename(image_path)
        new_image_path = os.path.splitext(image_path)[0] + ".png"
        image.save(new_image_path, "PNG")
        
        logger.info(f"Processed image saved as {new_image_path}")
        return new_image_path
    except Exception as e:
        logger.error(f"Error processing image {image_path}: {e}")
        return None

def process_all_images(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(root, file)
                process_image(image_path)

if __name__ == "__main__":
    base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'new_folder')
    process_all_images(base_dir)
