import numpy as np
import cv2

cap = cv2.VideoCapture('rgb_ball_720.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    ####
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_red_bound = np.array([0, 169, 112])
    u_red_bound = np.array([9, 255, 255])

    red_mask = cv2.inRange(img_hsv, l_red_bound, u_red_bound)

    kernel = np.ones((10,10), np.uint8)

    mask_no_noise = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)

    mask = cv2.morphologyEx(mask_no_noise, cv2.MORPH_OPEN, kernel)
    ##cv2.imshow("mask_opened", mask)

    segmented_img = cv2.bitwise_and(frame, frame, mask=mask)
    
    ####
    
    
    gray = cv2.cvtColor(segmented_img, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,0,255,0)
    
    M = cv2.moments(thresh)
    
    if M["m00"]!= 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
        
    cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
    cv2.putText(frame, "red ball", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    
    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)
    
    cv2.imshow('frame, click q to quit', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()