import cv2
import numpy
img=cv2.imread('bookpage.jpg')
####img=cv2.imread('book.jpg')
##img=cv2.imread('dark.jpg')
retval,threshold1=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)

cv2.imshow('real',img)
cv2.imshow('thresh',threshold1)
cv2.imshow('Gray2',threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()
