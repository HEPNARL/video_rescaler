import cv2
import os

input_folder_dir = "in"
# Desired output size (non-uniform allowed)
new_width = 100
new_height = 1080

for filename in os.listdir(input_folder_dir):
    if filename.lower().endswith((".mp4")):
        full_path = os.path.join(input_folder_dir, filename)
        print("Processing:", full_path)
        cap = cv2.VideoCapture(full_path)
        # Video writer setup
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter("./out/" + filename, fourcc, cap.get(cv2.CAP_PROP_FPS),
                            (new_width, new_height))
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # Resize frame to arbitrary size
            resized = cv2.resize(frame, (new_width, new_height),
                                interpolation=cv2.INTER_LINEAR)
            out.write(resized)
        cap.release()
        out.release()
