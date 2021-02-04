import numpy as np
import cv2 as cv

img=np.zeros((512, 512,3),np.uint8)
cv.rectangle(img, (0, 0), (400, 400), (0, 0, 255))
cv.line(img, (0, 0), (300, 300), (0, 255, 0), 10)
cv.circle(img,(250,250), 100,(255,0,0),cv.FILLED)
cv.putText(img,"HEY",(100,400),cv.FONT_ITALIC,1,(0,0,255),1)
cv.imshow("img", img)
cv.waitKey(0)