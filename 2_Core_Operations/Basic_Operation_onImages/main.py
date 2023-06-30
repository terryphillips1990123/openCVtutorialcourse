import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]

img1 = cv.imread('image.jpg')
assert img1 is not None, 'file could not be read, check with os.path.exists()'

replicate = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_CONSTANT, value = BLUE)

plt.subplot(321), plt.imshow(img1,'gray'), plt.title('ORIGINAL')
plt.subplot(322), plt.imshow(replicate,'gray'), plt.title('REPLICATE')
plt.subplot(323), plt.imshow(reflect,'gray'), plt.title('REFLECT')
plt.subplot(324), plt.imshow(reflect101,'gray'), plt.title('REFLECT_101')
plt.subplot(325), plt.imshow(wrap,'gray'), plt.title('WRAP')
plt.subplot(326), plt.imshow(constant,'gray'), plt.title('CONSTANT')

plt.show()