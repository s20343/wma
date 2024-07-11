# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:16:58 2023

@author: janle
"""

import numpy as np
import cv2 as cv
import cv2
from matplotlib import pyplot as plt

img = cv.imread('photo_1.jpg')
h = int(img.shape[0] / 1.5)
w = int(img.shape[1] / 1.5)
img = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)


# HARRIS
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv.goodFeaturesToTrack(gray,maxCorners = 4, qualityLevel=0.01,minDistance=150, useHarrisDetector=True,k=0.05)
corners = np.int0(corners)
print(corners[0].ravel())
for i in corners:
    x,y = i.ravel()
    #ravel return a contiguous flattened array.
    cv.circle(img,(x,y),10,255,-1)
plt.imshow(img),plt.show()






cv.imshow('harris_image',img)
# SIFT
image8bit = cv2.normalize(gray.copy(), None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
sift = cv.SIFT_create()
kp = sift.detect(image8bit,None)
kp, des = sift.detectAndCompute(image8bit,None)

image8bit=cv.drawKeypoints(image8bit,kp,img)
cv.imshow('sift_keypoints.jpg',image8bit)
cv.waitKey()
cv.destroyAllWindows()
cv.imwrite("01_cornerHarris_img.jpg", img)
cv.imwrite("01_Swift_img.jpg", gray)



