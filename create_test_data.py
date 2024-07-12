import os
from PIL import Image, ImageDraw

def create_test_image(image_path, size=(200, 200), color=(255, 0, 0)):
    image = Image.new("RGB", size, color)
    draw = ImageDraw.Draw(image)
    draw.text((size[0]//4, size[1]//4), "Test", fill=(255, 255, 255))
    image.save(image_path)

def create_test_folders(base_dir, num_folders=5, num_images_per_folder=3):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    for i in range(num_folders):
        folder_path = os.path.join(base_dir, f"product_{i+1}")
        os.makedirs(folder_path, exist_ok=True)
        for j in range(num_images_per_folder):
            image_path = os.path.join(folder_path, f"image_{j+1}.jpg")
            create_test_image(image_path)

if __name__ == "__main__":
    test_data_dir = "new_folder"
    create_test_folders(test_data_dir)
    print(f"Test folders and images created in '{test_data_dir}'")
