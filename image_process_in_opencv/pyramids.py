import cv2 as cv


img = cv.imread('../roi.jpg')

lower_reso = cv.pyrDown(higher_reso)

cv.imshow(lower_reso,'lower_reso')

cv.waitKey()
cv.destroyAllWindows()


