import cv2
import numpy as np

# Load the video file
cap = cv2.VideoCapture('res/rgb_ball_720.mp4')

# Check if the video was successfully opened
if not cap.isOpened():
    print("Error opening video file")

mask1 = None
mask2 = None

# Define the morphological kernel
kernel = np.ones((5, 5), np.uint8)

# Loop through each frame of the video
while cap.isOpened():
    # Read a new frame
    ret, frame = cap.read()

    # Convert to HSV format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask to isolate the red color range
    lower_red = np.array([0,195,134])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    #lower_red = np.array([170, 50, 50])
    #upper_red = np.array([180, 255, 255])
    #mask2 = cv2.inRange(hsv, lower_red, upper_red)

    #mask = cv2.bitwise_or(mask1, mask2)

    # Perform morphological operations to remove noise
    maskOpen = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernel)

    # Find the center of the red ball
    M = cv2.moments(mask1)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    # Add center of gravity and text to frame
    cv2.circle(frame, (cX, cY), 3, (0, 0, 0), -1)
    cv2.putText(frame, "Red ball", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Red ball tracking', frame)

    # closes video by pressing "q" key
    key = cv2.waitKey(25)
    if key == ord('q'):
           print('Closed')
           break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()


