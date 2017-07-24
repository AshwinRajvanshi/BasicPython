import cv2
import numpy as np
import pygame
import Matplotlib

bg = None

cap = cv2.VideoCapture(0)
def nothing(x):
    pass

#Kernel matrices for morphological transformation    
kernel_square = np.ones((11,11),np.uint8)
kernel_ellipse= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
while(True):
    _,frame = cap.read()
    blur = cv2.blur(frame,(3,3))
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    cv2.imshow('frame',frame)
    Roi = hsv[:,hsv.shape[1]/2:hsv.shape[1]]
    cv2.rectangle(hsv,(hsv.shape[1]/2,0),(hsv.shape[1],hsv.shape[0]),(0,255,0),1)
    cv2.rectangle(Roi,(Roi.shape[1]/4,0),(Roi.shape[1]/2,Roi.shape[0]/4),(0,255,0),3)
    cv2.rectangle(Roi,(Roi.shape[1]/4,Roi.shape[0]/2),(Roi.shape[1]/2,Roi.shape[0]),(255,0,0),3)
    cv2.imshow('Roi',Roi)
    
    #Create a binary image with where white will be skin colors and rest is black
    mask2 = cv2.inRange(Roi,np.array([2,50,50]),np.array([15,255,255]))
    dilation = cv2.dilate(mask2,kernel_ellipse,iterations = 1)
    erosion = cv2.erode(dilation,kernel_square,iterations = 1)    
    dilation2 = cv2.dilate(erosion,kernel_ellipse,iterations = 1)    
    filtered = cv2.medianBlur(dilation2,5)
    kernel_ellipse= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(8,8))
    dilation2 = cv2.dilate(filtered,kernel_ellipse,iterations = 1)
    kernel_ellipse= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    dilation3 = cv2.dilate(filtered,kernel_ellipse,iterations = 1)
    median = cv2.medianBlur(dilation2,5)
    ret,thresh = cv2.threshold(median,127,255,0)
    cv2.imshow('thresh',thresh)
    #find max contour
    _,contours, hierarchy =  cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)   
    max_area=0
    ci=0
    if len(contours)!=0:
        for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
    cnts=contours[ci]
    hull = cv2.convexHull(cnts)
    drawing = np.zeros(Roi.shape,np.uint8)
    cv2.drawContours(drawing, [cnts], 0, (0, 255, 0), 0)
    cv2.drawContours(drawing, [hull], 0,(0, 0, 255), 0)
    cv2.imshow('xxxx',drawing)
    
    k = cv2.waitKey(1)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
