import cv2 as cv
import numpy as np

# read in the image
img = cv.imread('res/tray7.jpg') #works for tray 3,7,8


# blur and convert to grayscale
img_blur = cv.medianBlur(img, 5)
img_gray = cv.cvtColor(img_blur, cv.COLOR_BGR2GRAY)

# get binary level photo and contours
ret, thresh = cv.threshold(img_gray, 105, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# find contour of the tray
imax = 0
areamax = 0
for i in range(len(contours)):
    if cv.contourArea(contours[i]) > areamax:
        imax = i
        areamax = cv.contourArea(contours[i])
tray = contours[imax]

# draw the contour of the tray
cv.drawContours(img, [tray], 0, (0,255,0), 3)

# find circles
circles = cv.HoughCircles(img_gray, cv.HOUGH_GRADIENT, 1, 10, param1=100, param2=35, minRadius=20, maxRadius=40)
circles = np.uint16(np.around(circles))

# draw the circles
for i in circles[0,:]:
    cv.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)
    cv.circle(img, (i[0], i[1]), 2, (0, 255, 0), 3)

# calculate coins
big_coin_in_tray = 0
small_coin_in_tray = 0
big_coin_out_tray = 0
small_coin_out_tray = 0
for i in circles[0,:]:
    if cv.pointPolygonTest(tray,(i[0],i[1]),False) >= 0:
        if i[2] > 31:
            big_coin_in_tray += 1
        else:
            small_coin_in_tray += 1
    else:
        if i[2] > 31:
            big_coin_out_tray += 1
        else:
            small_coin_out_tray += 1

# put text on image
img = cv.putText(img, "BigCoinInTray = "+str(big_coin_in_tray), (390,25), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 0, 0), 1)
img = cv.putText(img, "BigCoinOutTray = "+str(big_coin_out_tray), (390,50), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 0, 0), 1)
img = cv.putText(img, "SmallCoinInTray = "+str(small_coin_in_tray), (390,75), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 0, 0), 1)
img = cv.putText(img, "SmallCoinOutTray = "+str(small_coin_out_tray), (390,100), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 0, 0), 1)
img = cv.putText(img, "Area = "+str(areamax), (390,125), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 0, 0), 1)

# display results
img_res = cv.resize(img, (0, 0), fx=0.8, fy=0.8)
cv.imshow('Coins', img_res)
cv.waitKey(0)
cv.destroyAllWindows()
