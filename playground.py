import cv2
import numpy as np
import os


video_path = "/home/alex/Downloads/video2.mp4"

width, height = 1920, 1080
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    if isinstance(frame, type(None)) or cv2.waitKey(1) & 0xFF == ord('q'):
        break

    image = np.zeros((height, width, 3), dtype=np.uint8)
    fh, fw, _ = frame.shape
    ws = int(width/2 - fw/2)
    hs = int(height/2 - fh/2)
    image[hs:hs+fh, ws:ws+fw, :] = frame

    cv2.namedWindow('window', cv2.WND_PROP_FULLSCREEN)
    # cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
    cv2.setWindowProperty('window', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('window', image)

cap.release()
cv2.destroyAllWindows()


"""
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if isinstance(frame, type(None)) or cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('frame', frame)

cap.release()
cv2.destroyAllWindows()
"""

"""
# create image
image = np.ones((height, width, 3), dtype=np.float32)
image[:10, :10] = 0  # black at top-left corner
image[height - 10:, :10] = [1, 0, 0]  # blue at bottom-left
image[:10, width - 10:] = [0, 1, 0]  # green at top-right
image[height - 10:, width - 10:] = [0, 0, 1]  # red at bottom-right

window_name = 'projector'
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
# cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                      cv2.WINDOW_FULLSCREEN)
cv2.imshow(window_name, image)
cv2.waitKey()
cv2.destroyAllWindows()
"""
