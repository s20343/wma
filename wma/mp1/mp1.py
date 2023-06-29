# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys

# Load image
image = cv2.imread('res/red_ball.jpg')
if image is None:
    sys.exit("Could not load image")

# Convert to HSV format
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define red color range
lower_red = np.array([0, 50, 50])
upper_red = np.array([10 ,255 ,255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170, 50, 50])
upper_red = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

mask = cv2.bitwise_or(mask1, mask2)

# Perform morphological operations to remove noise
kernel = np.ones((5,5),np.uint8)
maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernel)

# Find the center of the red ball
M = cv2.moments(maskClose)
if M["m00"] != 0:
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
else:
    cX, cY = 0, 0

# Add center of gravity and text to image
cv2.circle(image, (cX, cY), 3, (0, 0, 0), -1)
cv2.putText(image, "Red ball", (cX - 30, cY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

# Display the image
cv2.imshow("Red ball detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

