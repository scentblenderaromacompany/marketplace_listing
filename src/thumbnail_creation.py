import os
from PIL import Image
from utils.logger import get_logger

logger = get_logger(__name__)

def create_thumbnail(image_path, size=(128, 128)):
    try:
        image = Image.open(image_path)
        image.thumbnail(size)
        base_name = os.path.basename(image_path)
        thumbnail_path = os.path.join(os.path.dirname(image_path), 'thumbnails', base_name)
        os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)
        image.save(thumbnail_path, "PNG")
        logger.info(f"Thumbnail created at {thumbnail_path}")
        return thumbnail_path
    except Exception as e:
        logger.error(f"Error creating thumbnail for {image_path}: {e}")
        return None

if __name__ == "__main__":
    test_image_path = 'path_to_your_test_image.png'
    thumbnail_path = create_thumbnail(test_image_path)
    if thumbnail_path:
        print(f"Thumbnail available at: {thumbnail_path}")
