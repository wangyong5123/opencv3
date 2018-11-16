import numpy as np
import cv2 as cv

from matplotlib import pyplot as plt


img = cv.imread('../roi.jpg',0)
edges = cv.Canny(img,100,200)


plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Org')
plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge image')
plt.xticks([]),plt.yticks([])

plt.show()
