import cv2 as cv
import os


img1 = cv.imread("/home/wy/code/opencv3_code/thunder.jpg")
#img2 = cv.imread("/home/wy/code/opencv3_code/opcv_l0og.png",0)

img2 = cv.imread("/home/wy/code/opencv3_code/logo.jpg")
print(img2.shape)

rows,cols,channel = img2.shape


roi = img1[0:rows,0:cols]


img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

cv.imshow('gray',img2gray)
cv.waitKey(0)


ret,mask = cv.threshold(img2gray,250,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)


cv.imshow('mask',mask)
cv.waitKey(0)

cv.imshow('mask_inv',mask_inv)
cv.waitKey(0)


img1_bg = cv.bitwise_and(roi,roi,mask=mask)
cv.imshow('bg',img1_bg)

cv.waitKey()
img2_fg = cv.bitwise_and(img2,img2,mask=mask_inv)
cv.imshow('fg',img2_fg)

cv.waitKey()
dst = cv.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst
cv.imshow('res',img1)

cv.waitKey(0)
cv.destroyAllWindows()
