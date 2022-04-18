import cv2
import numpy as np

cap = cv2.VideoCapture(0) #default cam.

while True:

  retVal, Frame = cap.read()

  if retVal:
    black_white = Frame.mean(axis=2)
    cv2.imshow("My Cam", black_white.astype(np.unit8))
    
  cv2.waitKey(10)
