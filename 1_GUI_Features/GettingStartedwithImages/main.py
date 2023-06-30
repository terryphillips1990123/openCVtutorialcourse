import cv2 as cv
import sys

img = cv.imread("image.jpg")

if img is None:
    sys.exit("Could not read the image.")
    pass

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("image1.png", img)