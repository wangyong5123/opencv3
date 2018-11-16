import numpy as np
import cv2

#BackgroundSubtractorMOG2
#opencv自带的一个视频
cap = cv2.VideoCapture('/home/wy/code/opencv3_code/video_analysis/A0008004.avi')
#创建一个3*3的椭圆核
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#创建BackgroundSubtractorMOG2
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    print(ret)

    cv2.imshow('frame',frame)
    
    fgmask = fgbg.apply(frame)
    #形态学开运算去噪点
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    #寻找视频中的轮廓
    im, contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        #计算各轮廓的周长
        perimeter = cv2.arcLength(c,True)
        if perimeter > 188:
            #找到一个直矩形（不会旋转）
            x,y,w,h = cv2.boundingRect(c)
            #画出这个矩形
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)    

    cv2.imshow('frame',frame)
    cv2.imshow('fgmask', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
