from PIL import Image, ImageOps
import os

def pad_to_aspect_ratio(img: Image.Image, target_ratio: float,fill_color=(0, 0, 0)) -> Image.Image:
    w, h = img.size
    current_ratio = w / h
    if current_ratio > target_ratio:
        # pad height (top & bottom)
        new_h = int(w / target_ratio)
        pad_top = (new_h - h) // 2
        pad_bottom = new_h - h - pad_top
        padding = (0, pad_top, 0, pad_bottom)

    elif current_ratio < target_ratio:
        # pad width (left & right)
        new_w = int(h * target_ratio)
        pad_left = (new_w - w) // 2
        pad_right = new_w - w - pad_left
        padding = (pad_left, 0, pad_right, 0)
    else:
        # already correct ratio
        return img
    return ImageOps.expand(img, padding, fill=fill_color)

def ratio_fit_images(path_in, path_out, size=(1920,1080), prior_ratio=3/2):
    for filename in os.listdir(path_in):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            full_path = os.path.join(path_in, filename)
            print("Processing:", full_path)
            img = Image.open(full_path)
            img = pad_to_aspect_ratio(img, prior_ratio)
            rescaled = img.resize(size)  # (width, height)
            rescaled.save(os.path.join(path_out, filename))

if __name__ == "__main__":
    ratio_fit_images("in", "out")