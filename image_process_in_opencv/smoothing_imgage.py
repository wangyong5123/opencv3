import numpy as np
import cv2 as cv

from matplotlib import pyplot as plt

img = cv.imread('../11.jpg')



"""
kernel = np.ones((2,2),np.float32)/4
dst = cv.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(dst),plt.title('Averageing')
plt.xticks([]),plt.yticks([])

plt.show()

"""

"""
blur2 = cv.blur(img,(2,2))
blur3 = cv.blur(img,(3,3))
blur5 = cv.blur(img,(5,5))
"""
blur2 = cv.blur(img,(2,2))
blur3 = cv.GaussianBlur(img,(3,3),0)

blur5 = cv.medianBlur(img,5)
blur6 = cv.bilateralFilter(img,9,75,75)


plt.subplot(2,2,1),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])

plt.subplot(2,2,2),plt.imshow(blur2),plt.title('Averageing 2*2')
plt.xticks([]),plt.yticks([])

plt.subplot(2,2,3),plt.imshow(blur3),plt.title('Averageing 3*3')
plt.xticks([]),plt.yticks([])

plt.subplot(2,2,4),plt.imshow(blur6),plt.title('Averageing 5*5')
plt.xticks([]),plt.yticks([])
plt.show()



