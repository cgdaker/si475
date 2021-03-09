import cv2
import numpy as np

# red
img = cv2.imread('red.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
outhsv = cv2.inRange(hsv,np.array([-3,15,15]),np.array([5,255,255]))
cv2.imwrite('kermit2.jpg',outhsv)
