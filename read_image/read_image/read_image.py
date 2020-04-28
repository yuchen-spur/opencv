# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('train.png',cv2.IMREAD_COLOR)

cv2.namedWindow('image',cv2.WINDOW_NORMAL) 
#先建一个可拖动大小的窗口
cv2.imshow('image',img)
#加载图片
k = cv2.waitKey(0) & 0XFF
#等待键盘在图像窗口输入
if k == ord('s'): 
    cv2.imwrite('new_train.jpg',img)
    #保存图像
    cv2.destroyAllWindows()
    #关闭所有窗口
elif k == 27:   #输入ESC
    cv2.destroyAllWindows()

plt.imshow(img,cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]),plt.yticks([])
plt.show()