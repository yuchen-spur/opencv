import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('OTSU.jpg',0)

ret1,th1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+ cv2.THRESH_OTSU)
#threshold_value,img = cv2.threshold(src,thresh,maxval,type[,dst])
blur = cv2.GaussianBlur(img,(5,5),0)
ret2,th2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+ cv2.THRESH_OTSU)


plt.subplot(2,3,1),plt.imshow(img,'gray')
plt.title('lisa'), plt.xticks([]), plt.yticks([]) # plt.xticks:刻度

plt.subplot(2,3,2),plt.hist(img.ravel(),256) # max = 256 的灰度直方图
plt.title('Histogram'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,3),plt.imshow(th1,'gray') 
plt.title('OTSU'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,4),plt.imshow(img,'gray')
plt.title('lisa'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,5),plt.hist(blur.ravel(),256)
plt.title('Histogram'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,6),plt.imshow(th2,'gray')
plt.title('BLUR_OTSU'), plt.xticks([]), plt.yticks([])

plt.show()


