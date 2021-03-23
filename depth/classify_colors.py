import cv2
import rospy
import numpy as np
from turtleAPI import robot

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


def avgColor(frame):
    # dimension - # of rows
    width = frame.shape[0]/2
    height = frame.shape[1]/2

    # get list of all non zero pizels and average
    count = 0
    sum = 0
    target_loc = cv2.findNonZero(frame)

    if (target_loc == None):
        return -1

    for x in target_loc:
        #print(type(x[0]))
	    sum += x[0][0]
        sumY += x[0][1]
        count += 1

    # calc average
    avg = sum/count
    yAvg = sumY/count

    # if no pixels in frame, ret -1
    # else return avg x coordinate - width
    return (avg - width, avg, yAvg)

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

def checkDepth(frame, xAvg, yAvg):
    # add buffer of ten
    x_low = xAvg - 5
    x_high = xAvg + 5
    y_low = yAvg - 5
    y_high = yAvg + 5

    # slice from the depth sensor
    slice = frame[x_low:x_high, y_low:y_high]

    # average constants
    sum = 0
    count = 0

    # avg distance
    for row in slice.shape[0]:
        for col in slice.shape[1]:

            # in nan add ten
            if slice[row, col].isnan():
                sum += 10
                count += 1
                continue

            # else add
            sum += slice[row, col]
            count += 1

    # average and check against depth val
    avg = sum/count
    print("avg: " + avg)
    if avg > 1:
        return True
    return False

# main
r = robot()
r.drive(angSpeed=.2)

# list and error for pid
error_list = []
old_error = 0
rate = rospy.Rate(20)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
ballColor = raw_input("What color balloon do you want to go to? ")
outhsv = None
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

while not rospy.is_shutdown():

    # get image and convert to the mask
    img = r.getImage()
    dpth = r.getDepth()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    pos = avgColor(outhsv)[0]

    #check depth
    if checkDepth(dpth, avgColor[1], avgColor[2]) == True:
        return

    # if no target color in frame, spin
    if pos == -1:
        r.drive(angSpeed=.2)
        continue

    # use pid to find angular speed
    ang_speed = pid_speed(-.005, 0, -.0001, pos, old_error, error_list)
    old_error = pos
    error_list.append(pos)

    # drive!
    r.drive(angSpeed=ang_speed, linSpeed=.3)
    print("pos: " + str(pos) + " angSpeed: " + str(ang_speed))
    rate.sleep()
