import numpy as np
import rospy
import time
from turtleAPI import robot

rob = robot()

r = rospy.Rate(5)

rob.drive(linSpeed=.3)

while not rospy.is_shutdown():
    depth = rob.getDepth()
    rows, cols = depth.shape
    
    depth = depth[(rows/3):,:]
    left = depth[:,(cols/5):(2*cols/5)]
    midd = depth[:,(2*cols/5):(3*cols/5)]
    righ = depth[:,(3*cols/5):(4*cols/5)]
    far_l = depth[:,:(cols/5)]
    far_r = depth[:,(4*cols/5)]
    
    midd = midd[np.logical_not(np.isnan(midd))]
    left = left[np.logical_not(np.isnan(left))]
    righ = righ[np.logical_not(np.isnan(righ))]
    far_l = far_l[np.logical_not(np.isnan(far_l))]
    far_r = far_r[np.logical_not(np.isnan(far_r))]
    
    midd = np.average(midd)
    righ = np.average(righ)
    left = np.average(left)
    far_l = np.average(far_l)
    far_r = np.average(far_r)
    
    count = 0
    for col in range(0, midd.shape[1]):
    
    print((far_l,left,midd,righ,far_r))
    
    if midd < .8:
        midd = 0
    turn = left-righ
    if far_l < 1:
        turn = -2
    if far_r < 1:
        turn = 2
    rob.drive(linSpeed=.35*midd,angSpeed=2*turn)
    r.sleep()

rob.stop()
