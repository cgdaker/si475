#import cv2
#import rospy
import math
import random
import argparse
import numpy as np
#from turtleAPI import robot

class Vertex:

    # all adjacent nodes are stored in each vertex's adj_nodes dictionary with the distance
    def __init__(self, label, x, y):
        self.label = label
        self.adj_nodes = {}
        self.x = float(x)
        self.y = float(y)

    # returns distance between this point and a given point
    def distance(self, x, y):
        diff_x = (self.x - x) ** 2
        diff_y = (self.y - y) ** 2
        return (diff_x + diff_y) ** .5

# parse args
parser = argparse.ArgumentParser(description='Navigate the robot to a given location')
parser.add_argument('path', metavar='p', type=str, help='path to DOT file')
parser.add_argument('coord', metavar='c', type=str, help='goal position')
parser.add_argument('start', metavar='s', nargs = "?", type=str, help='goal position')
args = parser.parse_args()

# read in all vertices
file = open(args.path, 'r')

#dict to hold the dicts
adj_matrix = {}
next(file)
for line in file:
    # check for the newline
    if line == '\n':
        break

    print(line)
    # read in the vertex
    line_parts = line.split('[')
    label = line_parts[0].strip(' ')
    coords = line_parts[1].split('"')[1].split(",")
    x = coords[0].strip('(')
    y = coords[1].strip(')')

    # create the vertex and add if not already in
    v = Vertex(label, x, y)
    adj_matrix[label] = v

# read in all edges
for line in file:
    #eof
    if not '--' in line:
        continue

    # split on edge
    edge = line.split('--')
    first_node = edge[0].strip(' ')
    second_node = edge[1].strip().replace(';', '')

    ''# get nodes from dictionary, add other node to each nodes dict
    v = adj_matrix[first_node]
    s = adj_matrix[second_node]
    v.adj_nodes[second_node] = v.distance(s.x, s.y)
    s.adj_nodes[first_node] = s.distance(v.x, v.y)

# make matrix
print(adj_matrix['A'].adj_nodes['C'])
