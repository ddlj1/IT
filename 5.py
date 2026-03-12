import cv2
import numpy as np

img1=cv2.imread('wall.png',cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('qr.png',cv2.IMREAD_GRAYSCALE)

orb=cv2.ORB_create()

kp1,des1=orb.detectAndCompute(img1,None)
kp2,des2=orb.detectAndCompute(img2,None)
bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches=bf.match(des1,des2)
matches=sorted(matches,key=lambda x:x.distance)
result=cv2.drawMatches(img1,kp1,img2,kp2,matches[:5],None,flags=2)
cv2.imshow("Matches",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
