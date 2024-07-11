
# %% imports
import numpy as np
import cv2 as cv
import cv2
import sys
# %% colours 
 
cGreen = (0,255,0)
cRed = (0,0,255)
cBlue = (255,255,0)
cYellow = (0,255,255)
# %% image work
img = cv2.imread("tray7.jpg", cv2.IMREAD_COLOR)
if img is None:
    sys.exit("Could not read the image.")
   
imgBlur = cv2.medianBlur(img, 11)
cimg = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
#%%

ret, thresh = cv2.threshold(cimg, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#%%
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
cv2.drawContours(img, [tray], 0, cYellow, 3)
img = cv2.putText(img,"Area = "+str(areamax), (50,50),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1.0, color=(255,255,255), thickness=1)

#%% find circles

circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 1, 30, param1=15,param2=40,minRadius=10,maxRadius=50)
circles = np.uint16(np.around(circles))


smallCoinsInside = 0
smallCoinsOutside = 0
bigCoinsInside = 0
bigCoinsOutside = 0


radiuses = np.transpose(circles[0])[2]
maxRadius = max(radiuses)


for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],cGreen,2)
    cv2.circle(img,(i[0],i[1]),2,cGreen,3)
    
    point = (i[0],i[1])
    result = cv2.pointPolygonTest(tray, point, False)
    if result > 0:
        if i[2] > maxRadius - 5:
            bigCoinsInside += 1
        else: 
            smallCoinsInside += 1
    if result < 0:
        if i[2] > maxRadius - 5:
            bigCoinsOutside+= 1
        else: 
            smallCoinsOutside += 1
    
    
    
allCoinsInside = smallCoinsInside + bigCoinsInside;
allCoinsOutside = smallCoinsOutside + bigCoinsOutside;

print("Big coins in the tray: ", bigCoinsInside)
print("Small coins in the tray: ",smallCoinsInside)
print("Big coins outside the tray: ",bigCoinsOutside)
print("Small coins outside the tray: ",smallCoinsOutside)

img =  cv2.putText(img,"bigCoinsInside = "+str(bigCoinsInside), (50,250),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1.0, color=(255,255, 255), thickness=1)
img =  cv2.putText(img,"smallCoinsInside = "+str(smallCoinsInside), (50,300),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1.0, color=(255,255, 255), thickness=1)
img =  cv2.putText(img,"smallCoinsOutside = "+str(smallCoinsOutside), (50,350),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1.0, color=(255,255, 255), thickness=1)
img =  cv2.putText(img,"bigCoinsOutside = "+str(bigCoinsOutside), (50,400),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1.0, color=(255,255, 255), thickness=1)


imgRes = cv2.resize(img, (0,0), fx=0.8, fy=0.8) 
cv.imshow('COINS',imgRes)
cv.waitKey(0)



