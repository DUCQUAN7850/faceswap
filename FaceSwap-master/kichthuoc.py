import cv2
import numpy as np
import math

img = cv2.imread('imgs/test1.jpg')
print(img.shape)
# res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
height, width = img.shape[:2]
res = cv2.resize(img,(math.floor(width/4), math.floor(height/4)), interpolation = cv2.INTER_CUBIC)
print(res.shape)
cv2.imshow("sadas",res)
cv2.imshow("sdad",img)
cv2.waitKey(20000)