import cv2
import numpy as np

def nothing(x):
    pass

alpha = 0

img1 = cv2.imread('house.jpg')
img2 = cv2.imread('seaside.jpg')

cv2.namedWindow('image')
#cv2.createTrackbar('alpha','image',0,100,nothing)


while 1 :
    #alpha = cv2.getTrackbarPos('alpha','image')
    alpha += 1
    dst = cv2.addWeighted(img1,alpha/2000,img2,1-alpha/2000,0)
    cv2.imshow('image',dst)
    if  alpha == 2000 or cv2.waitKey(1) == 27 :
        break

cv2.destroyAllWindows()
    

