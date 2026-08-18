import cv2
import numpy as np
import time

# ---- Cloak HSV range (yellow) ----
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([35, 255, 255])

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Stand out of frame. Capturing background in 3 seconds...")
time.sleep(3)

# ---- Step 1: Capture and average background ----
num_frames = 60
backgrounds = []

for i in range(num_frames):
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.flip(frame, 1)
    backgrounds.append(frame.astype(np.float32))

background = np.mean(backgrounds, axis=0).astype(np.uint8)
print("Background captured. Starting invisibility effect... Press Q to quit.")

# ---- Step 2: Live loop ----
kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create mask for cloak color
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Clean up mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=1)

    # Inverse mask: everything that's NOT the cloak
    mask_inv = cv2.bitwise_not(mask)

    # Cloak area -> pulled from background
    cloak_area = cv2.bitwise_and(background, background, mask=mask)

    # Non-cloak area -> pulled from current frame
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine both
    final_output = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)

    cv2.imshow("Invisible Cloak", final_output)
    cv2.imshow("Mask (debug)", mask)  # keep this open while tuning, remove later

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()