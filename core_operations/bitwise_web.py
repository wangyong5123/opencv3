import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load two images
img1 = cv2.imread('thunder.jpg')
img2 = cv2.imread('logo.jpg')


print(img2.shape)
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',img2gray)
cv2.waitKey(0)
#img2gray = cv2.bitwise_not(img2gray)
#ret, mask = cv2.threshold(img2gray, 50, 255, cv2.THRESH_BINARY)
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.imshow('mask_inv',mask_inv)
cv2.waitKey(0)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('bg',img1_bg)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow('fg',img2_fg)
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.waitKey(0)
cv2.imshow('result',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
