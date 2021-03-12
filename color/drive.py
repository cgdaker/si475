import math, rospy
from turtleAPI import robot

#error function for angle
def angleDiff(cur_angle, desired):
    # calculate difference
    diff = cur_angle - desired
    while diff > math.pi:
        diff -= 2*math.pi
    while diff < -math.pi:
        diff += 2*math.pi

    #if (abs(diff) < .1):
    #	if diff > 0: return .1
    #    if diff < 0: return -.1

    if (abs(diff) > 3):
        if diff > 0: return 3
        if diff < 0: return -3

    return diff

# error function for position
def posDiff(current, desired):
    #calculate component differences
    x_diff = current[0] - desired[0]
    y_diff = current[1] - desired[1]

    #calculate the total distance
    return (x_diff**2 + y_diff**2)**.5

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
