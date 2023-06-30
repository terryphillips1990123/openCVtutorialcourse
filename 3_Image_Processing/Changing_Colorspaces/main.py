import cv2 as cv
import numpy as np

cap = cv.VideoCapture("AngryBird.mp4")

while(1):
    # Take each frame
    _, frame = cap.read()
    if frame is None:
        break
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_RGB2HSV)
    # Define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask = mask)
    frame = cv.resize(frame, (640, 480))
    mask = cv.resize(mask, (640, 480))
    res = cv.resize(res, (640, 480))
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k==27:
        break
cv.waitKey(0)
# cv.destroyAllWindows()