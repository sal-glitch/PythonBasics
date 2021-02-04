import numpy as np
import cv2 as cv

img=cv.imread("resources/lena.png")
hor=np.hstack((img,img))
cv.imshow("img", hor)
cv.waitKey(0)
ver=np.vstack((img,img))
cv.imshow("img", ver)
cv.waitKey(0)