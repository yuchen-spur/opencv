import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

img = cv2.imread('edge.jpg',0)
blur_img = cv2.GaussianBlur(img,(5,5),0)#最后一个是标准差

cv2.namedWindow('image')#一定要有
cv2.createTrackbar('Min','image',100,1255,nothing)
cv2.createTrackbar('Max','image',200,1255,nothing)

while(1):
    min_val = cv2.getTrackbarPos('Min','image')#39
    max_val = cv2.getTrackbarPos('Max','image')#178
    edges = cv2.Canny(img,min_val,max_val)#下阈值和上阈值为1:2或1:3

    cv2.imshow('image',edges)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
    
    
