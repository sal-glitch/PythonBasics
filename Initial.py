import cv2
import numpy as np
img=cv2.imread("resources/lena.png")
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#odd number kernel size gaussian blur
imgblur=cv2.GaussianBlur(imggray,(7,7),0)
imgcanny=cv2.Canny(img,130,200)
kernel=np.ones((5,5),np.uint8)
imgdial=cv2.dilate(imgcanny,kernel,iterations=1 )
imger=cv2.erode(imgdial,kernel,iterations=1)
cv2.imshow("output",imger)
cv2.waitKey(0)

#CROPPING AND RESIZING
print(img.shape)
#width height
imgr=cv2.resize(img,(300,200))

#height width
imgcrop=imgr[0:200,100:150]
cv2.imshow("two",imgcrop)
cv2.waitKey(0)
cap=cv2.VideoCapture("some path")
while True:
   success,img=cap.read()
  cv2.imshow("videw",img)
 if cv2.waitKey(1) &0xFF==ord('o'):
    break

#Using webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
#brightness
cap.set(10,100)
while True:
    success,img = cap.read()
    cv2.imshow("Video" , img)
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break

