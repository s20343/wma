import numpy as np
import cv2 as cv
imgOrignal = cv.imread('tray8.jpg', cv.IMREAD_COLOR)
imgBlur = cv.medianBlur(imgOrignal,21)  
imgGray = cv.cvtColor(imgBlur,cv.COLOR_BGR2GRAY)
#%%
ret, thresh = cv.threshold(imgGray, 127, 255, 0)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#%%
#finding tray countour by looking for the countour with the biggest area
imax=0
areamax=0
for i in range(len(contours)):
    temp = contours[i]
    area = cv.contourArea(temp)
    if area > areamax:
        imax=i
        areamax=area
tray = contours[imax]
area = cv.contourArea(tray)
cv.drawContours(imgOrignal, [tray], 0, (0,255,0), 3)
#%%
imgOrignal = cv.putText(imgOrignal,"Area = "+str(areamax), (50,250),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1.0, color=(255,0,0), thickness=1)
imgRes = cv.resize(imgOrignal, (0,0), fx=0.8, fy=0.8) 
cv.imshow('COINS',imgRes)
cv.waitKey(0)
cv.destroyAllWindows()
