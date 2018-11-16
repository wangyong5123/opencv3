import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

cap  = cv.VideoCapture('1.avi')


while(cap.isOpened()):
	ret,frame = cap.read()
	
	grap = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

	cv.imshow('frame',gray)
	
	if cv.waitKey(1) & 0XFF == ord('q'):
		break

cap.release()
cv.destroyAllWindows()
