import cv2
from PIL import Image
im = Image.open('test_l3.jpg')
im_rotate = im.rotate(348)
im = im_rotate.save("hello.jpg")
img = cv2.imread('hello.jpg',0)
cv2.imshow('circle and dot', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
