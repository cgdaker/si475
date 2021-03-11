import rospy
import cv2
from turtleAPI import robot

# frame is 639 pixels

# function to take in the array and return three averages for each third of the frame
# returns tuple of averages for each third
def getAverages(frame):
    rows = frame.shape[0]

    # get slices
    size_slice = rows/3
    first_third = frame[:, 0:size_slice]
    second_third = frame[:, size_slice:size_slice*2]
    third_third = frame[:, size_slice*2:rows]

    # average each
    left_average = first_third.average()
    mid_average = second_third.average()
    right_average = third_third.average()

    return (left_average, mid_average, right_average)

r = robot()
while not rospy.is_shutdown():
    dpth = r.getDepth()
