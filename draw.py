import numpy as np
import cv2
from time import strftime,localtime

# create a black image。
img = np.zeros((512,512,3),np.uint8)

# draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)
# draw a full green rectangle
cv2.rectangle(img,(384,0),(510,128),(0,255,0),-1)
# draw a red circle
cv2.circle(img,(447,63),63,(0,0,255),3)
# draw a ellipse
cv2.ellipse(img,(256,256),(100,50),45,0,360,(255,255,0),-1)
# draw a ploygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2)) # N*1*2
cv2.polylines(img,[pts],True,color=(0,0,255),thickness=3) # [pts]
# add Text
font = cv2.FONT_HERSHEY_SIMPLEX
text = str(strftime("%Y-%m-%d %H:%M:%S",localtime()))
cv2.putText(img,text,(10,500),font,1,(255,255,255),1)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyWindow('img')
