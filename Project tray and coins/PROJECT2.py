# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:42:20 2023

@author: janle
"""
# %% imports
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
# %% colours 
 
cGreen = (0,255,0)
cRed = (0,0,255)
cBlue = (255,255,0)
cYellow = (0,255,255)
# %% image work
img = cv2.imread("tray1.jpg")
if img is None:
    sys.exit("Could not read the image.")
   
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# %% tray 
edges =  cv2.Canny(cimg,  700, 800, apertureSize = 5)

lines = cv2.HoughLines(edges, 1, np.pi/180, 90,)


x1 =lines[1][0][0]
x2 =lines[1][0][0]
y1 =lines[0][0][1]
y2 =lines[0][0][1]
for line in lines:
    
    if x1 > line[0][0]:
        x1 = line[0][0]
    if x2 < line[0][0]:
        x2 = line[0][0]
    if y1 > line[0][1]:
        y1 = line[0][1]
    if y2 < line[0][1]:
        y2 = line[0][1]
    


cv2.line(img, (int(x1),int(y1)), (int(x2),int(y2)),cRed,2)
cv2.line(img, (int (x1),int(y1)), (int(x1),int(y2)),cGreen,2)
cv2.line(img, (int(x2),int(y2)), (int(x2),int(y1)),cBlue,2)
cv2.line(img, (int(x2),int(y2)),(int(x1),int(y2)),cYellow,2)
 
plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

cv2.imshow("aaaa",cimg) 
cv2.imshow("aaaa",img) 
cv2.waitKey()

#%%

circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 1, 30, param1=15,param2=40,minRadius=10,maxRadius=50)
circles = np.uint16(np.around(circles))

smallCoinsInside = 0
smallCoinsOutside = 0
bigCoinsInside = 0
bigCoinsOutside = 0


for i in circles[0,:]:  
    if i[0]>x1 and i[0]<x2 and i[1]>y1 and i[1]<y2:
        smallCoinsInside += 1
        bigCoinsInside += 1
        cv2.circle(img,(i[0],i[1]),i[2],cGreen,2)
    else:
        smallCoinsOutside += 1
        bigCoinsOutside += 1
      

cv2.imshow('circles', img)
cv2.waitKey()
