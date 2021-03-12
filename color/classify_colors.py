import cv2
import numpy as np

# constants
red_lower = np.array([-3,15,15])
red_upper = np.array([5,255,255])
blue_lower = np.array([115, 15, 15])
blue_upper = np.array([125, 255, 255])

# red
img = cv2.imread('blue.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
outhsv = cv2.inRange(hsv,blue_lower,blue_upper)
cv2.imwrite('kermit2.jpg',outhsv)
