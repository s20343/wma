import numpy as np
import cv2 as cv

img = cv.imread('res/photo_1.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray,maxCorners = 4, qualityLevel=0.01,minDistance=100,useHarrisDetector=True,k=0.04)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),10,255,-1)

cv.imshow('Detected Corners', img)
cv.waitKey()
cv.destroyAllWindows()


sift = cv.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)
img_with_keypoints=cv.drawKeypoints(gray,kp,img)

cv.imshow('Detected Keypoints', img_with_keypoints)
cv.waitKey()
cv.destroyAllWindows()

