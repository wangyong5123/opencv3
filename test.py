import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#second params error   cv.cCV_LOAD_IMAGE_COLOR
#Ok IMREAD_COLOR IMREAD_GRAYSCALE 



img = cv.imread("/home/wy/code/opencv3_code/text_384_384.jpg")

#img1 = np.zeros((512,512,3),np.uint8)

#     image start  end     color    pix
cv.line(img,(0,0),(511,511),(255,0,0),5)

#           image start   end       color  pix
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

#         image  start     color    pix
cv.circle(img,(100,63),63,(0,0,255),-1)



cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))

cv.polylines(img,[pts],True,(0,255,255))

#font = cv.FONT_HERSHEY_SIMPLEX
#cv.putText(img,"OpenCV",(10,500),font,4,(255,255,255),2,cv.LINE_AA)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,200), font, 2,(255,255,255),2,cv.LINE_AA)

"""
plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
plt.xticks([])
plt.yticks([])
plt.show()
"""
#
"""
print(img.shape)
print(img.size)

print(img.dtype)
"""
#cv.namedWindow('image',cv.WINDOW_NORMAL)


#cv.nameWindow("Image")
cv.imshow("Image",img)

#################
#font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX,1,1,0,3,8)


################

print("waitkey")

k = cv.waitKey(0)

if k == 27:
	cv.destoryAllWindows()
elif k == ord('s'):
	cv.imwrite('messgray.jpg',img)
	cv2.destroyAllWindows()
