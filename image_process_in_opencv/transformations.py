import numpy as np
import cv2 as cv

img = cv.imread('../opencv_logo.png',0)

rows,cols = img.shape

cv.imshow('image1',img)
cv.waitKey(0)


#res = cv.resize(img,None,fx=0.5,fy=0.5,interpolation = cv.INTER_CUBIC)

"""
M = np.float32([[1,1,100],[1,0,50]])
dst = cv.warpAffine(img,M,(cols,rows))
"""

"""
M = cv.getRotationMatrix2D(((cols -1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))
"""

"""
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
"""

"""
perspective transformation

"""

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv.getPerspectiveTransform(pts1,pts2)

dst = cv.warpPerspective(img,M,(300,300))


cv.imshow('image2',dst)
cv.waitKey(0)

cv.destroyAllWindows()
