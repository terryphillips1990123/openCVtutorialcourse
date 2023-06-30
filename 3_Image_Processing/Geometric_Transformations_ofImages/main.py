import numpy as np
import cv2 as cv

img = cv.imread('1.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, 'file could not be read, check with os.path.exists()'
rows, cols = img.shape
tz = 100
ty = 200
M = np.float32([[1, 0, tz], [0, 1, ty]])
dst = cv.warpAffine(img, M, (cols, rows))
M1 = cv.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), 290, 1)
dst1 = cv.warpAffine(img, M1, (cols, rows))
cv.imshow('img', dst)
cv.imshow('img1', dst1)
cv.imwrite('shifted_image.jpg', dst)
cv.imwrite('rotated_image.jpg', dst1)
cv.waitKey(0)
cv.destroyAllWindows()