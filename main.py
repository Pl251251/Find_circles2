import cv2
import math
import numpy as np
import imutils



img = cv2.imread('Oval_shape.jpg',0)
height, width = image.shape[:2]
center = (width/2, height/2)

rotate_matrix = cv2.getRotationMatrix2D(center, 348, 1)
rotated = cv2.warpAffine(img, rotate_matrix, (width, height))


"""
rotated = imutils.rotate_bound(img, 12)
cv2.imshow('oval', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

x_1 = int((rotated.shape[1]) * (8.5/(math.sqrt(230))))
resized_ = cv2.resize(img,(x_1, rotated.shape[0]))

cv2.imshow('oval', resized_)
cv2.waitKey(0)
cv2.destroyAllWindows()




#finding a circle
blur= cv2.medianBlur(resized_,7)
gray = cv2.cvtColor(blur,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=100,maxRadius=120)
info = np.uint16(np.around(circles))
a=0
for i in info[0,:]:
    cv2.circle(resized_,(i[0],i[1]),i[2],(255,0,0),2)
    cv2.circle(resized_,(i[0],i[1]),2,(0,0,255),3)

img =resized_
x_2 = int((img.shape[1]) * ((math.sqrt(230)/8.5)))
resized2_ = cv2.resize(img,(x_2, img.shape[0]))

rotate_matrix = cv2.getRotationMatrix2D(center, 12, 1)
rotated = cv2.warpAffine(resized2_, rotate_matrix, (width, height))


cv2.imshow('oval', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()"

