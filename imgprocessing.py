import numpy as np
import cv2 as cv
img = cv.imread("resources/shape4.jpg")
imgcontour=img.copy()

def getcountours(img):
    contours,hier=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for c in contours:
        area=cv.contourArea(c)
        print(area)
        if area>500:
            cv.drawContours(imgcontour, c, -1, (255, 0, 0))
            peri=cv.arcLength(c,True)
            print(peri)
            approx=cv.approxPolyDP(c,0.02*peri,True)
            objcor=len(approx)
            x,y,w,h=cv.boundingRect(approx)
            if objcor==3: objtype="Triangle"
            else: objtype="None"
            cv.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),2)
            cv.putText(imgcontour,objtype,
                       (x+(w//2)-10,y+(h//2)-10),
                       cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2
                       )

imggra=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(imggra,(7,7),1)
can=cv.Canny(blur,50,50)
cv.imshow("img",img)
cv.imshow("graybl",blur)
cv.imshow("can",can)
getcountours(can)
cv.imshow("contour",imgcontour)
cv.waitKey(0)
