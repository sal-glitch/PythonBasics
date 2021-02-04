import numpy as np
import cv2 as cv

img=cv.imread("resources/kings.jpg")
width,height=250,350
pts1=np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv.getPerspectiveTransform(pts1,pts2)
imgop=cv.warpPerspective(img,matrix,(width,height))
cv.imshow("orig img", img)
cv.imshow("warped img", imgop)
cv.waitKey(0)