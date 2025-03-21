import numpy as np
import rospy
import time
import math
from turtleAPI import robot

rob = robot()

r = rospy.Rate(5)

rob.drive(linSpeed=.3)

def checkIfClose(midd):
    print(midd.shape)
    if len(midd.shape) == 1:
        return True
    #only
    for col in range(0, midd.shape[1]):
        count = 0
        sum = 0
        for row in range(0, midd.shape[0]/2): #only want lower half
            if math.isnan(midd[row][col]):
                continue

            sum += midd[row][col]
            count += 1

        #avg for this col
        avg = sum/count
        if avg < 1.5:
            return False
            print('col average less than 0')

        return True

while not rospy.is_shutdown():
    depth = rob.getDepth()
    rows, cols = depth.shape
    go = True
    l = True
    go_right = True

    depth = depth[(rows/3):,:]
    left = depth[:,(cols/5):(2*cols/5)]
    midd = depth[:,(2*cols/5):(3*cols/5)]
    righ = depth[:,(3*cols/5):(4*cols/5)]
    far_l = depth[:,:(cols/5)]
    far_r = depth[:,(4*cols/5)]

    go = checkIfClose(midd)

    midd = midd[np.logical_not(np.isnan(midd))]
    left = left[np.logical_not(np.isnan(left))]
    righ = righ[np.logical_not(np.isnan(righ))]
    far_l = far_l[np.logical_not(np.isnan(far_l))]
    far_r = far_r[np.logical_not(np.isnan(far_r))]

    mid = np.average(midd)
    righ = np.average(righ)
    left = np.average(left)
    far_l = np.average(far_l)
    far_r = np.average(far_r)

    print((far_l,left,mid,righ,far_r))

    if mid < .8:
        mid = 0
    turn = left-righ
    if far_l < 1:
        turn = -2
    if far_r < 1:
        turn = 2

    if go == False:
        mid = 0
        if turn > 0:
            turn = 4
        else:
            turn = -4

    rob.drive(linSpeed=.25*mid,angSpeed=2*turn)
    r.sleep()

rob.stop()
