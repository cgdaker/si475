import cv2
import numpy as np
img = cv2.imread('pink.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
outhsv = cv2.inRange(hsv, np.array([304, 15, 15]), np.array([309,255,255]))
cv2.imwrite('pink2.jpg', outhsv)
