import cv2 

imgpath = "text_384_384.bgr"

img = cv2.imread("./text_384_384.bgr")

cv2.imshow("Image",img)

cv2.waitKey(0)
