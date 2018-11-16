import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

img = cv.imread('../logo.jpg')

#kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))

kernel = cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
#kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
print(kernel)
#kernel = np.ones((5,5),np.uint8)

erosion = cv.erode(img,kernel,iterations = 1)
dilation = cv.dilate(img,kernel,iterations = 1)

opening = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
closing = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)


gradient = cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel)
tophat = cv.morphologyEx(img,cv.MORPH_TOPHAT,kernel)

blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

plt.subplot(3,3,1),plt.imshow(img),plt.title('img')
plt.xticks([]),plt.yticks([])

plt.subplot(3,3,2),plt.imshow(erosion),plt.title('erosion')
plt.xticks([]),plt.yticks([])

plt.subplot(3,3,3),plt.imshow(dilation),plt.title('dilation')
plt.xticks([]),plt.yticks([])

plt.subplot(3,3,4),plt.imshow(opening),plt.title('opening')
plt.xticks([]),plt.yticks([])

plt.subplot(3,3,5),plt.imshow(closing),plt.title('closing')
plt.xticks([]),plt.yticks([])

plt.subplot(3,3,6),plt.imshow(gradient),plt.title('gradient')
plt.xticks([]),plt.yticks([])
plt.subplot(3,3,7),plt.imshow(tophat),plt.title('tophat')
plt.xticks([]),plt.yticks([])

plt.subplot(3,3,8),plt.imshow(blackhat),plt.title('blackhat')
plt.xticks([]),plt.yticks([])
plt.show()
