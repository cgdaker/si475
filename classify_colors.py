import cv2
import numpy as np

# constants
red_lower = np.array([-3,15,15])
red_upper = np.array([5,255,255])
pink_lower = np.array([295, 15, 15])
pink_upper = np.array([310, 100, 100])
green_lower= np.array([55, 15, 15])
green_upper= np.array([65, 255, 255])

# red
img = cv2.imread('green.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
outhsv = cv2.inRange(hsv,green_lower,green_upper)
cv2.imwrite('kermit2.jpg',outhsv)
