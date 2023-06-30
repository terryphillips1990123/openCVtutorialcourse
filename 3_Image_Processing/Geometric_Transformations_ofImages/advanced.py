import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('input.png')
assert img is not None, 'file could not be read, check with os.path.exists()'

pts1 = np.float32([[115, 106], [400, 103], [33, 481], [484, 482]])
pts2 = np.float32([[10, 10], [502, 10], [10, 502], [502, 502]])

M = cv.getPerspectiveTransform(pts1, pts2)

dst = cv.warpPerspective(img, M, (512, 512))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()