import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

img=cv2.imread('qr.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3,minSize=(30,30))
for(x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(w+x,y+h),(255,0,0),2)

cv2.imshow('detectfaces',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
