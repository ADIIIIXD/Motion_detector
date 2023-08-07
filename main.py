import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1)

while True:
    check, frame = video.read()
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey_frame, (5, 5), 0)
    cv2.imshow("my_video", blur)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
