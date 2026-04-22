import cv2
import os

def compute_padding(w, h, target_ratio):
    current_ratio = w / h
    if current_ratio > target_ratio:
        new_h = int(w / target_ratio)
        pad_top = (new_h - h) // 2
        pad_bottom = new_h - h - pad_top
        return (pad_top, pad_bottom, 0, 0)
    elif current_ratio < target_ratio:
        new_w = int(h * target_ratio)
        pad_left = (new_w - w) // 2
        pad_right = new_w - w - pad_left
        return (0, 0, pad_left, pad_right)
    return (0, 0, 0, 0)


def rescale_videos(path_in, path_out, size=(1920,1080), target_ratio=3/2):
    for filename in os.listdir(path_in):
        if filename.lower().endswith((".mp4")):
            full_path = os.path.join(path_in, filename)
            print("Processing:", full_path)
            cap = cv2.VideoCapture(full_path)
            # Video writer setup
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            out = cv2.VideoWriter(os.path.join(path_out, filename), fourcc, cap.get(cv2.CAP_PROP_FPS), size)
            while True:
                ret, frame = cap.read()
                if not ret:
                    break         
                h, w = frame.shape[:2]
                pad_t, pad_b, pad_l, pad_r = compute_padding(w, h, target_ratio=target_ratio)
                padded = cv2.copyMakeBorder(frame,pad_t, pad_b, pad_l, pad_r,cv2.BORDER_CONSTANT,value=(0, 0, 0))
                # Resize frame to arbitrary size
                resized = cv2.resize(padded, size, interpolation=cv2.INTER_LANCZOS4)
                # smoothed = cv2.GaussianBlur(resized, (9, 9), sigmaX=10)
                out.write(resized)
            cap.release()
            out.release()
