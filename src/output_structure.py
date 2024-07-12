import os
import shutil
from datetime import datetime

def organize_output(base_dir):
    timestamp = datetime.now().strftime("%m-%d-%Y_%I-%M_%p")
    sku_start = 1
    sku_end = 0

    new_base_dir = f"{base_dir}_{timestamp}_Processed_SKU-{sku_start}-{sku_end}"
    os.makedirs(new_base_dir, exist_ok=True)

    for root, dirs, files in os.walk(base_dir):
        for dir_name in dirs:
            product_dir = os.path.join(root, dir_name)
            sku_end += 1
            sku_dir = os.path.join(new_base_dir, f"SKU_{sku_start:05d}")
            os.makedirs(sku_dir, exist_ok=True)

            # Move files
            for file_name in os.listdir(product_dir):
                src_file = os.path.join(product_dir, file_name)
                dest_file = os.path.join(sku_dir, file_name)
                shutil.move(src_file, dest_file)
            
            # Create thumbnails folder
            thumbnails_dir = os.path.join(sku_dir, "thumbnails")
            os.makedirs(thumbnails_dir, exist_ok=True)

            # Create metadata folder
            metadata_dir = os.path.join(sku_dir, "metadata")
            os.makedirs(metadata_dir, exist_ok=True)

            # Save SKU info
            with open(os.path.join(sku_dir, "SKU.txt"), "w") as sku_file:
                sku_file.write(f"SKU_{sku_start:05d}")

            sku_start += 1

    new_base_dir = f"{base_dir}_{timestamp}_Processed_SKU-1-{sku_end}"
    shutil.move(base_dir, new_base_dir)
    print(f"Organized output saved to {new_base_dir}")

if __name__ == "__main__":
    base_dir = "/workspaces/marketplace_listing/new_folder"
    organize_output(base_dir)
