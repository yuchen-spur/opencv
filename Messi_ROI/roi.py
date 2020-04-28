import cv2
import numpy as np

img1=cv2.imread('Messi.png')
img2=cv2.imread('opencv_logo.png')#黑底

rows,cols,channels  = img2.shape
roi = img1[0:rows,0:cols]
# part of img1

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 15, 255, cv2.THRESH_BINARY)
# create pure black-white image as mask 
mask_inv = cv2.bitwise_not(mask)
#create inverse mask


img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# cv2.bitwise_and(src，dst，mask=)
# white part can be changed and black part is fixed
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)


dst = cv2.add(img1_bg,img2_fg)
# black part can be changed and white part not
img1[0:rows, 0:cols ] = dst
# put new roi on the src
cv2.imshow('res',img1)
cv2.imwrite('Messi&logo.png',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
