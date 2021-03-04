from drive import *
from turtleAPI import robot
import cv2

r = robot()
while True:
    print(r.getAngle()[2])

    angle = float(input("Angle: "))
    while ( abs(r.getAngle()[2] - angle) > .05 ):
        print(r.getAngle())
        r.drive(angSpeed=.1)
    
    r.drive(angSpeed=0)
    img = r.getImage()
    cv2.imwrite('image_' + str(angle) + '.jpg', img)
