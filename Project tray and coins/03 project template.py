import numpy as np
import cv2 as cv
"""
The code and text below is a proposed solution to the project,
but it is not mandatory.
These are loose suggestions as to how the lecturer would solve the problem
posed in the project.
"""
#%%
#import image, blur it, and convert to grayscale colorspace
#imgOrignal = cv.imread()
#imgBlur = cv.medianBlur()  
#imgGray = cv.cvtColor()
#%%
#get binary lvl photo and contours
#ret, thresh = cv.threshold()
#contours, hierarchy = cv.findContours()
#%%
#find contour of the TRAY - it is contour with the biggest area - using for loop and if condition
#imax=0
#areamax=0
#for i in range(len(contours)):
#    if cv.contourArea(contours[i]) > areamax:
#        imax=...
#        areamax=cv.contourArea()
#tray = contours[imax]
#where imax is the number of the contour with the biggest area
#area = cv.contourArea()
#cv.drawContours()
#%%
#find circles
#circles = cv.HoughCircles()
#circles = np.uint16(np.around(circles))
#draw circles
#for i in circles[0,:]:
    # draw the outer circle
#    cv.circle()
    # draw the center of the circle
#    cv.circle()
#%%
#calculate coins
#BigCoinInTray=0
#SmallCoinInTray=0
#BigCoinOutTray=0
#SmallCoinOutTray=0
#for i in circles[0,:]:
#    if cv.pointPolygonTest()>-1:
#        if ... > ...:
#            BigCoinInTray=BigCoinInTray+1
#        else:
#            SmallCoinInTray=SmallCoinInTray+1
#   else:
#        if ... > ...:
#            BigCoinOutTray=BigCoinOutTray+1
#        else:
#            SmallCoinOutTray=SmallCoinOutTray+1

#imgOrignal = cv.putText(imgOrignal,"BigCoinInTray = "+str(BigCoinInTray), (50,50),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1.0, color=(255,0,0), thickness=1)
#imgOrignal = cv.putText(imgOrignal,"BigCoinOutTray = "+str(BigCoinOutTray), (50,100),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1.0, color=(255,0,0), thickness=1)
#imgOrignal = cv.putText(imgOrignal,"SmallCoinInTray = "+str(SmallCoinInTray), (50,150),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1.0, color=(255,0,0), thickness=1)
#imgOrignal = cv.putText(imgOrignal,"SmallCoinOutTray = "+str(SmallCoinOutTray), (50,200),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1.0, color=(255,0,0), thickness=1)
#imgOrignal = cv.putText(imgOrignal,"Area = "+str(areamax), (50,250),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1.0, color=(255,0,0), thickness=1)

#%%
#display results
#imgRes = cv.resize(imgOrignal, (0,0), fx=0.8, fy=0.8) 
#cv.imshow('COINS',imgRes)
#cv.waitKey(0)
#cv.destroyAllWindows()