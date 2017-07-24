import cv2
import numpy
from Tkinter import *
from tkFileDialog   import askopenfilename      

def callback():
    name= askopenfilename() 
    print name
    
errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X)

mainloop()
cv2.waitKey(0)
cv2.destroyAllWindows()



##img=cv2.imread('bookpage.jpg') let x be the name of the image
##retval,threshold1=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
##grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##retval2,threshold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
##gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
##cv2.imshow('real',img)
##cv2.imshow('thresh',threshold1)
##cv2.imshow('Gray2',threshold2)
##cv2.imshow('gaus',gaus)

