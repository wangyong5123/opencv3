import numpy as np
import cv2 as cv
img = cv.imread('../opencv_logo.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#cnt = contours[4]

cv.drawContours(img,contours,3,(0,255,0),3)

cv.imshow(img,'img')

cv.waitKey(0)

cv.destroyAllWindows()

print(contours,hierarchy)
