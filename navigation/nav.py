#import cv2
import rospy
import math
import random
import argparse
import numpy as np
from turtleAPI import robot

class Vertex:

    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "main":

    # parse args
    parser = argparse.ArgumentParser(description='Navigate the robot to a given location')
    parser.add_argument('path', metavar='p', type=str, help='path to DOT file')
    parser.add_argument('coord', metavar='c', type=str, help='goal position')
    parser.add_argument('--start', metavar='s', type=str, nargs='+',
                        help='goal position')

    args = parser.parse_args()
    
    # read in all vertices

    # read in all edges

    # make matrix
