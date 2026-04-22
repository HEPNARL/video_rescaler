import cv2
import os

def rescale_videos(path_in, path_out, size=(1920,1080)):
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
                # Resize frame to arbitrary size
                resized = cv2.resize(frame, size, interpolation=cv2.INTER_LANCZOS4)
                # smoothed = cv2.GaussianBlur(resized, (9, 9), sigmaX=10)
                out.write(resized)
            cap.release()
            out.release()
