import cv2
import rospy
import math
import random
import numpy as np
from turtleAPI import robot

# constants
red_lower = np.array([-3,15,15])           # done
red_upper = np.array([5,255,255])          # done
pink_lower = np.array([145, 15, 15])       # done
pink_upper = np.array([155, 255, 255])     # done
green_lower= np.array([70, 15, 15])        # done
green_upper= np.array([80, 255, 255])      # done
blue_lower = np.array([110, 100, 40])       # done
blue_upper = np.array([130, 255, 255])     # done
yellow_lower = np.array([25, 15, 15])       # done
yellow_upper = np.array([35, 255, 255])     # done

def avgColor(frame):
    print("here")
    # dimension - # of rows
    width = frame.shape[0]/2
    dpth = r.getDepth()
    count = 0
    flag = False

    # get list of all non zero pizels and average
    count = 0
    sum = 0
    target_loc = cv2.findNonZero(frame)
    depthSum = 0
    #r = Random()

    if (target_loc == None):
        return -1

    print(type(target_loc))
    print("here2 \n")

    # for x in target_loc:
    #     row = x[0][1]
    #     col = x[0][0]
    #     count += 1
    #
    #     sum += x[0][0]
    #     count += 1
    #
    #     depthSum += dpth[row][col]

    sum = 1
    count = 1
     
    # for i in range(0, 5):
    #     rand = r.

    # calc average
    avg = sum/count
    # if not nan check and exit if close
    print(depthSum/count)
    if not math.isnan(depthSum/count):
        if depthSum/count < .5:
            print("arrived! distance: " + str(depthSum/count))
            r.drive(angSpeed=0, linSpeed=0)
            exit(0)

    # if no pixels in frame, ret -1
    # else return avg x coordinate - width
    return avg - width, count

# pid
def pid_speed(kp, ki, kd, error, old_error, error_list):

    # add the error to the integral portion
    if len(error_list) > 5:
        error_list.pop()
    error_list.append(error)

    #calculate sum
    error_sum = 0
    for i in error_list:
        error_sum += i

    # kp portion + ki portion
    to_return = (kp * error) + (ki * error_sum)
    to_return += kd * (error - old_error)

    return to_return

def check_in_frame(pos, frame):

    if pos == -1:
        return True

    count = np.sum(frame == 255)
    print("Count: " + count)

# main
ballColor = raw_input("What color balloon do you want to go to? ")

r = robot()
r.drive(angSpeed=.1)

# list and error for pid
error_list = []
old_error = 0
rate = rospy.Rate(20)
while not rospy.is_shutdown():

    # get image and convert to the mask
    img = r.getImage()
    img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


    outhsv = 0
    if ballColor == "red":
        # red
        outhsv = cv2.inRange(hsv,red_lower,red_upper)
    elif ballColor == "blue":
        # blue
        outhsv = cv2.inRange(hsv,blue_lower,blue_upper)
    elif ballColor == "green":
        # green
        outhsv = cv2.inRange(hsv,green_lower,green_upper)
    elif ballColor == "yellow":
        # yellow
        outhsv = cv2.inRange(hsv,yellow_lower,yellow_upper)
    elif ballColor == "pink":
        # pink
        outhsv = cv2.inRange(hsv,pink_lower,pink_upper)
    else:
        print("Invalid color choice. Quitting")
        quit()

    #cv2.imshow('balloon.jpg', outhsv)
    #cv2.waitKey(0)
    pos, count = avgColor(outhsv)

    # if no target color in frame, spin
    if count < 3000:
        r.drive(angSpeed=.1)
        continue

    # use pid to find angular speed
    ang_speed = pid_speed(-.005, 0, -.0001, pos, old_error, error_list)
    old_error = pos
    error_list.append(pos)

    # drive!
    r.drive(angSpeed=ang_speed, linSpeed=.10)
    print("pos: " + str(pos) + " angSpeed: " + str(ang_speed))
    rate.sleep()
