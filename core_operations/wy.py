import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("/home/wy/code/opencv3_code/test.jpg")

#img = cv.imread("/home/wy/code/opencv3_code/text_384_384.jpg")
print(img.size)

cv.imshow("Image",img)

print("waitkey")

k = cv.waitKey(0)

cv.destroyAllWindows()
