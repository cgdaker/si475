#import cv2
#import rospy
import math
import random
import argparse
from driver import driver
import numpy as np
import sys
import dijkstra as dij
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
        #print(self.x, x)
        diff_x = (self.x - x) ** 2
        #print(diff_x)
        diff_y = (self.y - y) ** 2
        #print(diff_y)
        return (diff_x + diff_y) ** .5

# finds and adds vertex to the node closest - used for goal and starting
def find_closest(goal_vertex, adj_matrix):
    closest_node = None
    closest_dist = 1000
    for key in adj_matrix:
        this_vertex = adj_matrix[key]
        dist = this_vertex.distance(goal_vertex.x, goal_vertex.y)

        # first time through loop
        if closest_node == None:
            closest_node = this_vertex
            closest_dist = dist
            continue

        # check for min
        if dist < closest_dist:
            closest_node = this_vertex
            closest_dist = dist

    # add the edges between goal and closest to goal_coords
    goal_vertex.adj_nodes[closest_node.label] = goal_vertex.distance(closest_node.x, closest_node.y)
    closest_node.adj_nodes[goal_vertex.label] = closest_node.distance(goal_vertex.x, goal_vertex.y)
    print("Closest node: " + closest_node.label)

# just put in list of nodes to drive to
def drive(node_list, robot):
    for node in node_list:
        driver.run(node.x, node.y, robot)

# parse args
parser = argparse.ArgumentParser(description='Navigate the robot to a given location')
parser.add_argument('path', metavar='p', type=str, help='path to DOT file')
parser.add_argument('coord', metavar='c', type=str, help='goal position')
parser.add_argument('start', metavar='s', nargs = "?", type=str, help='goal position')
args = parser.parse_args()

if len(sys.argv) == 4:
    third_arg = True
else:
    third_arg = False

print(third_arg)
# read in all vertices
file = open(args.path, 'r')
goal_coords = args.coord

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

# create goal node
coords = goal_coords.split(',')
x_goal = coords[0].strip()
y_goal = coords[1].strip()

# add all distances for goal
goal_vertex = Vertex("Goal", x_goal, y_goal)
find_closest(goal_vertex, adj_matrix)

r = Robot()
if third_arg:
    start_coords = args.start.split(",")
    x_goal = coords[0].strip()
    y_goal = coords[1].strip()
else:
    #robot get mcl pose
    pos = r.getMCLPose()
    x_goal = #robot x coord
    y_goal = #robot y coord

# make vertex and get closest
start = Vertex("Start", x_goal, y_goal)
find_closest(start, adj_matrix)

# make matrix
#print(adj_matrix['1a'].adj_nodes['2a'])
print(adj_matrix["1b"].adj_nodes["Goal"])
print("\n")
dij.dijkstra(adj_matrix, '1a')
