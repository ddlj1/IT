import cv2

image=cv2.imread(r"C:\Users\manthan\Desktop\test\qr code.png")
cv2.imshow("image",image)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
resize=cv2.resize(image,(200,200))
cv2.imshow("rezie",resize)
(h,w)=image.shape[:2]
center=(w//2,h//2)
M=cv2.getRotationMatrix2D(center,45,1.0)
rotated=cv2.warpAffine(image,M,(w,h))
cv2.imshow("rotation",rotated)
cropped=image[50:200,100:300]
cv2.imshow("copped",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
