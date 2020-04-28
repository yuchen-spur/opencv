import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):#mouse callback function
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
# window1 for record events
cv2.setMouseCallback('image',draw_circle)
# bind window1 to function
# this method record event and x,y as draw_circle parament
    
while (1):
    cv2.imshow('image',img)
    print('1')
    # window2 for show results ,can be not the same as window1
    if cv2.waitKey(20)&0xFF == 27:
        break

cv2.destroyAllWindows()
