#import required libraries 
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time 

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

test1 = cv2.imread('imgs/test11.jpg')
gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)

haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);

crop_img=test1[0:0,0:0]
for (x, y, w, h) in faces:
    # cv2.rectangle(test1, (x-25, y-50), (x+w+40, y+h+40), (255, 0, 255), 2)
    crop_img = test1[y-y:y+h+h, x:x+w]	

# cv2.imshow("abc",convertToRGB(test1))
# crop_img=crop_img[0:0,0:0]
cv2.imshow("cropped", crop_img)
print(test1.shape)
print(crop_img.shape)   
cv2.waitKey(5000)
cv2.destroyAllWindows()