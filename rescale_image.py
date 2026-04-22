from PIL import Image
import os

input_folder_dir = "in"
out = "out"

def rescale_images(path_in, path_out, size=(1920,1080)):
    for filename in os.listdir(path_in):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            full_path = os.path.join(path_in, filename)
            print("Processing:", full_path)
            img = Image.open(full_path)
            rescaled = img.resize(size)  # (width, height)
            rescaled.save(os.path.join(path_out, filename))
