import cv2
import numpy as np

# red
img = cv2.imread('red.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
outhsv = cv2.inRange(hsv,np.array([358,60,20]),np.array([0,255,235]))
cv2.imwrite('kermit2.jpg',outhsv)
