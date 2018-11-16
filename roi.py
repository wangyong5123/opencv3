import cv2 as cv
import numpy as np

srcImg = cv.imread('test.jpg')

cv.namedWindow('scrImage',cv.WINDOW_AUTOSIZE)

cv.imshow('scrImage',srcImg)

img_roi_y = 100
img_roi_x = 100
img_roi_height = 50
img_roi_width = 50

#img_roi = srcImg[img_roi_y:(img_roi_y+img_roi_height),img_roi_x:(img_roi_x+img_roi_width)]


img_roi = srcImg[img_roi_y:(img_roi_y+img_roi_height),img_roi_x:(img_roi_x+img_roi_width)]

cv.namedWindow("ROI_img",cv.WINDOW_AUTOSIZE)
cv.imshow("ROI_img",img_roi)

cv.imwrite('wy.jpg',img_roi)

cv.waitKey(0)
cv.destroyWindow("scrImage")
cv.destroyWindow("ROI_img")
