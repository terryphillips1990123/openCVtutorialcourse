import cv2 as cv

img = cv.imread("2.jpg")
print(cv.useOptimized())
img1 = cv.medianBlur(img, 49)
cv.imshow('blur', img1)
cv.waitKey(0)
