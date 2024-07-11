# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:25:19 2023

@author: Jan Malicki _s22264

"""
# -*- coding: utf-8 -*-

# %% TASK 1 - IMAGE
import cv2 
import sys
import numpy as np
##Import libraries: cv2 (OpenCV), numpy, sys (1 point).

img = cv2.imread("red_ball.jpg")
##cv2.imshow("RedBall", img)
##Import photo ball.png (1 point).

if img is None:
    sys.exit("Could not read the image.")
##Set the condition for the correct loading of the image, e.g. using the 'sys.exit' command (1 point).




img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

l_red_bound = np.array([150, 100, 100])
u_red_bound = np.array([179, 255, 255])

red_mask = cv2.inRange(img_hsv, l_red_bound, u_red_bound)
#Change the image format to HSV (1 point).


kernel = np.ones((10,10), np.uint8)

mask_no_noise = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)

mask = cv2.morphologyEx(mask_no_noise, cv2.MORPH_OPEN, kernel)
##cv2.imshow("mask_opened", mask)
#Improve image quality (remove noise) through morphological operations (1 point).


segmented_img = cv2.bitwise_and(img, img, mask=mask)
#Find the colours using a binary operation (1 point).



cv2.imshow("mask after removing noises", mask)

contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
temp_output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
#cv2.imshow("temp_output", temp_output)

output = cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
#cv2.imshow("output", output)


ret,thresh = cv2.threshold(mask,127,255,0)
#cv2.imshow("Threwsh", thresh)


M = cv2.moments(thresh)
 
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
 
cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
#Add the calculated centre of gravity of the ball to the image (1 point).

cv2.putText(img, "red ball", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#Add the word "red ball" near the centre of gravity (1 point).
 
 
cv2.imshow("Image", img)
cv2.waitKey(0)




