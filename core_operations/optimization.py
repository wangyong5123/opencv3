
import cv2 as cv
img1 = cv.imread('opencv_logo.png')

cv.imshow('image',img1)
cv.waitKey(0)

e1 = cv.getTickCount()
for i in range(5,49,2):
	img1 = cv.medianBlur(img1,i)

#cv.useOptimzed()

#%timeit res = cv.medianBlur(img,49)


e2 = cv.getTickCount()

t = (e2 - e1)/cv.getTickFrequency()

print(t)


cv.imshow('image2',img1)
cv.waitKey(0)
cv.destroyAllWindows()
