#To determine if a point is inside, outside, or on the edge of a shape you can check if the point is within a contour using cv2.pointPolygonTest().
import cv2

image = cv2.imread('rectangle.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

rect = contours[1] #I have chosen arbitrary contour, e.g. 1
point1 = (25, 50)
point2 = (200, 250)
# Perform check if point is inside contour/shape
cv2.drawContours(image, [rect], 0, (36, 255, 12), 2)
result1 = cv2.pointPolygonTest(rect, point1, False)
result2 = cv2.pointPolygonTest(rect, point2, False)
"""
pointPolygonTest the third argument is measureDist:
True, it finds the shortest distance between a point in the image and a contour.
False, it finds whether the point is inside, outside, or on the contour.
"""

# Draw points
cv2.circle(image, point1, 8, (100, 100, 255), -1)
cv2.putText(image, 'point1', (point1[0] -10, point1[1] -20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), lineType=cv2.LINE_AA)
cv2.circle(image, point2, 8, (200, 100, 55), -1)
cv2.putText(image, 'point2', (point2[0] -10, point2[1] -20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), lineType=cv2.LINE_AA)

print('If 1 is inside , point1:', result1)
print('If 1 is inside , point2:', result2)
#The function returns +1, -1, or 0 to indicate if a point is inside, outside, or on the contour, respectively

cv2.imshow('image', image)
cv2.waitKey()