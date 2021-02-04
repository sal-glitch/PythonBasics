import numpy as np
import cv2 as cv
def f(x): return x
cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars",640,240)
cv.createTrackbar("Hue Min","Trackbars",0,179,f)
cv.createTrackbar("Hue Max","Trackbars",19,179,f)
cv.createTrackbar("Sat Min","Trackbars",110,255,f)
cv.createTrackbar("Sat Max","Trackbars",240,255,f)
cv.createTrackbar("Val Min","Trackbars",153,255,f)
cv.createTrackbar("Val Max","Trackbars",255,255,f)
img = cv.imread("resources/lambo.png")
imghsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
while True:
    hmin = cv.getTrackbarPos("Hue Min","Trackbars" )
    hmax = cv.getTrackbarPos("Hue Max", "Trackbars")
    smin = cv.getTrackbarPos("Sat Min", "Trackbars")
    smax = cv.getTrackbarPos("Sat Max", "Trackbars")
    vmin = cv.getTrackbarPos("Val Min", "Trackbars")
    vmax = cv.getTrackbarPos("Val Max", "Trackbars")
    print(hmin,hmax,smin,smax,vmin,vmax)
    lower=np.array([hmin,smin,vmin])
    upper=np.array([hmax,smax,vmax])
    mask=cv.inRange(imghsv,lower,upper)
    imgres=cv.bitwise_and(img,img,mask=mask)
    cv.imshow("filter",imgres)
    cv.imshow("img", imghsv)
    cv.imshow("Mask",mask)
    cv.waitKey(1)
    if cv.waitKey(1) & 0xFF == ord('p'):
        break
