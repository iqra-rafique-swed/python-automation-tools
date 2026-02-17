from PIL import Image
import os

def convert_images(input_folder, output_folder, target_format="png"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img = Image.open(os.path.join(input_folder, filename))
            base_name = os.path.splitext(filename)[0]
            new_file = f"{base_name}.{target_format}"
            img.save(os.path.join(output_folder, new_file))
            print(f"Converted: {filename} → {new_file}")

# Example usage:
# convert_images("images", "converted_images", "png")
