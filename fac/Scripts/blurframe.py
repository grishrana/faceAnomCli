import cv2 as cv
import os

filename = "harcascade_frontalface_default.xml"
path = os.path.dirname(__file__)

harr_class = cv.CascadeClassifier(os.path.join(path, filename))


def blurframe(frame):
    frame = cv.flip(frame, 1)
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    face_rect = harr_class.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=3)

    for x, y, w, h in face_rect:
        frame[y : y + h, x : x + w, :] = cv.blur(
            frame[y : y + h, x : x + w, :], (30, 30)
        )

    return frame
