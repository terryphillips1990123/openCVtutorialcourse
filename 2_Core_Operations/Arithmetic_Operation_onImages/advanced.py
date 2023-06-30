import cv2 as cv
import numpy as np
img1 = cv.imread('1.jpg')
img2 = cv.imread('logo.png')

gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
mask = np.zeros(gray.shape).astype('uint8')

mask[np.where(gray < 245)] = 0

cv.imshow('mask', mask)

cv.waitKey(0)