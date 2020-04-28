import numpy as np
import cv2

cap = cv2.VideoCapture('Covid-19.mp4')#Covid-19.mp4
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#1920
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#1080
fps = int(cap.get(cv2.CAP_PROP_FPS))#25


fourcc = cv2.VideoWriter_fourcc(*'XVID')# set decode method
out = cv2.VideoWriter('output.mp4',fourcc,25,(width,height))
# create VideoWriter obj (name,encode method,play rate,(width,height))

while (cap.isOpened()):
    ret,frame = cap.read()# read one frame from cap
    if ret == 1:# read frame OK? the last frame return False
       
        #M = cv2.getRotationMatrix2D((width/2,height/2),90 , 1.0)
        #frame = cv2.warpAffine(frame, M, (width,height))
        frame = np.rot90(frame)
        # frame=cv2.flip(frame,0)
        # 0:垂直翻转，1：水平翻转，-1：水平垂直翻转

        out.write(frame)  # save the flipped frame
        cv2.imshow('frame',frame)# show the frame
        if cv2.waitKey(25)&0xFF == 27:
            break
    else :
        break
cap.release()
out.release()
cv2.destroyAllWindows()
