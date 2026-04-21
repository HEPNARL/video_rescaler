from PIL import Image
import os

input_folder_dir = "in"

for filename in os.listdir(input_folder_dir):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        full_path = os.path.join(input_folder_dir, filename)
        print("Processing:", full_path)
        img = Image.open(full_path)
        rescaled = img.resize((1920, 1080))  # (width, height)
        rescaled.save("./out/" + filename)
