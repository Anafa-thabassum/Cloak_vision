import cv2 
import numpy as np
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Stand out of frame. Capturing background in 3 seconds...")
time.sleep(3)

num_frames = 60
backgrounds = []

for i in range(num_frames):
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.flip(frame, 1)  # keep mirrored, consistent with live feed
    backgrounds.append(frame.astype(np.float32))

# Average all captured frames into one stable background
background = np.mean(backgrounds, axis=0).astype(np.uint8)

cv2.imwrite("assets/background_sample.jpg", background)
print("Background captured and saved to assets/background_sample.jpg")

cv2.imshow("Captured Background", background)
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()