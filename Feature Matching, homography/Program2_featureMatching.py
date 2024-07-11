# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:42:26 2023

@author: janle
"""

# import required libraries
import numpy as np
import cv2 as cv
import cv2
import matplotlib.pyplot as plt

# read two input images as grayscale
img1 = cv2.imread('photo_2_query.jpg',0)
img2 = cv2.imread('photo_2_train.jpg',0)

img1 = cv.imread("photo_2_query.jpg", cv.IMREAD_GRAYSCALE) # queryImage
img1 = cv.resize(img1, (0, 0), fx = 0.5, fy = 0.5)
img2 = cv.imread("photo_2_train.jpg", cv.IMREAD_GRAYSCALE) # trainImage
img2 = cv.resize(img2, (0, 0), fx = 0.5, fy = 0.5)

# Initiate SIFT detector
sift = cv.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# Brute-Force matcher 'BFMatcher' is simple.
# It takes the descriptor of one feature in first set
# and is matched with all other features in second set using some distance calculation.
# And the closest one is returned.
# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.50*n.distance:
        good.append([m])
# cv.drawMatchesKnn expects list of lists as matches.
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3),plt.show()
cv.imwrite("02_FeatureMatcher.jpg", img3)
