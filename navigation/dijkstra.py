import math


# Numbered steps are copied from https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

# create Node class
class Node:
    def __init__(self, key, adjacent):
        self.name = key
        self.neighbors = adjacent
        self.visited = False
        self.parent = None

def dijkstra(matrix, destinationKey):
    #1 Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.

    # create set of unvisited nodes
    unvisitedNodes = []
    unvisitedKeys = []
    for key in matrix:
        node = Node(key, matrix[key].adj_nodes)
        unvisitedNodes.append(node)
        unvisitedKeys.append(key)
        if(key == destinationKey):
            destinationNode = node

    #2 Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.

    # set distance for all nodes
    for node in unvisitedNodes:
        node.value = float('inf')
        #print(node.name + " " + str(node.value))

    # set initial node as current and distance value to zero
    current = unvisitedNodes[0]
    current.value = 0

    while(True):
        #3 For the current node, consider all of its unvisited neighbours and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbour B has length 2, then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.

        # iterate through all unvisited neighbors and calculate distances

        #print(unvisited[0].neighbors['2a'])
        #print(current.name)
        for key in current.neighbors:
            
            try:
                neighborIndex = unvisitedKeys.index(key)
                neighborNode = unvisitedNodes[neighborIndex]
                
                # distance from current node to given neighbor
                dis = current.neighbors[key]
                newDistance = current.value + dis
                
                if(newDistance < neighborNode.value):
                    neighborNode.value = newDistance
                    neighborNode.parent = current
                    #print(newDistance)

            except ValueError:
                pass
                #print("Not found")

        #4 When we are done considering all of the unvisited neighbours of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.

        # mark the current as visited
        current.visited = True

        # remove it from the unvisited set
        unvisitedNodes.remove(current)
        unvisitedKeys.remove(current.name)


        #5 If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
        if(destinationNode.visited == True):
            #print("algorithm complete: output answer here")
            print(getParents(destinationNode))
            break
        
        #6 Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 3.
        else:
            current = unvisitedNodes[0]
            for node in unvisitedNodes:
                if(current.value > node.value):
                    current = node

def getParents(node):

    if(node.parent == None):
        return node.name
    else:
        return getParents(node.parent) + " " + node.name
