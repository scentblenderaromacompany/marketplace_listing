from PIL import Image

def create_test_image(path, size=(100, 100), color=(255, 0, 0)):
    image = Image.new("RGB", size, color)
    image.save(path)

if __name__ == "__main__":
    test_image_path = "new_folder/product_1/image_1.png"
    create_test_image(test_image_path)
    print(f"Test image created at {test_image_path}")
