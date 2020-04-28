import cv2
import numpy as np

yellow = np.uint8([[[216,224,225]]])
hsv_yellow = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)
print(hsv_yellow)


cap = cv2.VideoCapture('yellow.mp4')

while (cap.isOpened()) :    
    ret,frame = cap.read()
    if cv2.waitKey(1) == 27 or ret==False:
        break
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([15,150,152])
    upper_yellow = np.array([27,250,252])#need to adjust

    mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
    #trans to black-white

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
cv2.destroyAllWindows()

