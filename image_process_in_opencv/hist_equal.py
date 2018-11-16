
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../wiki.jpg',0)

equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side


cv.imwrite('../res.png',res)

cv.destroyAllWindows()
"""

clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize = (8,8))

cll = clahe.apply(img)

cv.imwrite('clahe_2.jpg',cll)

cv.destroyAllWindows()
"""
