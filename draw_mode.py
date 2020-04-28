import cv2
import numpy as np

ix,iy = -1,-1
mood = 1

def draw_mode(event,x,y,flags,param):#在event发生的任意时刻执行
    global ix,iy,mood,b,g,r

    if mood==1:
        if event==cv2.EVENT_LBUTTONDOWN:
            ix,iy = x,y
        elif event==cv2.EVENT_MOUSEMOVE and \
             flags==cv2.EVENT_FLAG_LBUTTON:
            cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
            
    elif mood==2:
        if event==cv2.EVENT_LBUTTONDOWN:
            ix,iy = x,y
        elif event==cv2.EVENT_MOUSEMOVE and \
             flags==cv2.EVENT_FLAG_LBUTTON:
            ra =int( np.sqrt((x-ix)**2+(y-iy)**2))
            cv2.circle(img,(ix,iy),ra,(b,g,r),-1)

def nothing(x):
    pass

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_mode)

cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

switch='0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while (1):
    cv2.imshow('image',img)
    if cv2.waitKey(1)&0xFF == 27 :
        break
    elif cv2.waitKey(1)&0xFF == ord('m') :
        #waitkey(0)导致不能自动刷新
        mood = 2

    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    s=cv2.getTrackbarPos(switch,'image')
    
    
cv2.destroyAllWindows()
    
