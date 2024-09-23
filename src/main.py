import cv2
from camera import Camera
import time

camera = Camera()

time.sleep(2)

while True:
    ret, frame = camera.get_frame()

    if not ret or frame is None:
        continue

    print(f"Frame dimensions: {frame.shape}")

    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow('Raw Frame', frame_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
