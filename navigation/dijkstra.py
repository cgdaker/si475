import math


# Numbered steps are copied from https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

# create Node class
class Node:
    def __init__(self, key, adjacent):
        self.name = key
        self.neighbors = adjacent

def dijkstra(matrix):
    #1 Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.

    print(matrix['1a'].adj_nodes['2a'])
    # create set of unvisited nodes
    unvisited = []
    for key in matrix:
        unvisited.append(Node(key, matrix[key].adj_nodes))

    #2 Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.

    # set distance for all nodes
    for node in unvisited:
        node.value = float('inf')

    # set initial node as current and distance value to zero
    current = unvisited[0]
    current.value = 0

    #3 For the current node, consider all of its unvisited neighbours and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbour B has length 2, then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.

    # iterate through all unvisited neighbors and calculate distances

    #print(unvisited[0].neighbors['2a'])
    for key in unvisited[0].neighbors:
        print(key)

    #for neighbor in current.neighbors:
        #newDistance = current.value + 0 # TODO: the distance from current to neighbor
        #if(newDistance < neighbor.value


    #4 When we are done considering all of the unvisited neighbours of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.


    #5 If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.

    #6 Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 3.
