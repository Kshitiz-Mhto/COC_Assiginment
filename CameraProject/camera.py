import cv2
from google.colab.patches import cv2_imshow
import datetime

cap = cv2.VideoCapture(1) #providing capturing feature
out = cv2.VIdeoWriter('output.avi', -1,20.0,(720,640))

while True:
  retvalue, image = cap.read()
  # print (retvalue) #----> ensure that read() is providing frame or not
  # print (type(image))  --->numpy ndarray
  # print(image.shape)    ---> provide the shape of your web cam
  # cv2.imshow("My CAM", image)
  if revalue:
    cv2_imshow("My Cam",image)
    out.write(image)
  key = cv2.waitKey(5)  # --->wait for the next capture in 5 miliseconds and provide an unique unicode value

  if key == ord('q'):
    break
  if key == ord('c'):
    now = datetime.now()
    date_time = now.strftime("%Y_%m_%d__%H:%M:%s")
    cv2.imwrite('{}.png'.format(date_time), image)
  
#   while working for the multiple task done by single app
cap.release() 
cv2.destoryAllWindows()
out.release()
