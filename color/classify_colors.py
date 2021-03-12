import cv2
import numpy as np

# constants
red_lower = np.array([-3,15,15])           # done
red_upper = np.array([5,255,255])          # done
pink_lower = np.array([145, 15, 15])       # done
pink_upper = np.array([155, 255, 255])     # done
green_lower= np.array([70, 15, 15])        # done
green_upper= np.array([80, 255, 255])      # done
blue_lower = np.array([115, 15, 15])       # done
blue_upper = np.array([125, 255, 255])     # done
yellow_lower = np.array([25, 15, 15])       # done
yellow_upper = np.array([35, 255, 255])     # done

# red
img = cv2.imread('yellow.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
outhsv = cv2.inRange(hsv,yellow_lower,yellow_upper)
cv2.imwrite('kermit2.jpg',outhsv)
