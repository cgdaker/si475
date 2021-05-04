from state import State
from Queue import PriorityQueue
import json
#from turtleAPI import robot
from map import Map
from drive import Driver

def get_nodelist(path):


    #open file and iterate
    file = open(path, 'r')
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

def aStar(root):
    # make pq
    pq = PriorityQueue()
    visited_states = {}

    s = root
    # -1 indicates this is goal state
    while (s.get_heuristic() != -1):
        # get list of all adjacent states
        adj_states = s.get_possible_states()

        # check if in visited - if yes, replace state with one from visted dict
        # for state in adj_states:
        #     if state.to_string() in visited_states:
        #         print("already seen")
        #         adj_states.remove(state)
        #         adj_states.append(visited_states[state.to_string()])
        #         continue

            # else add the state
            # print( ' adding new: ' + state.to_string())
            # visited_states[state.to_string()] = state

        for state in adj_states:
            if s.to_string() == state.to_string():
                continue

            # check if adjacent states already in graph - if so use the already seen state
            if state.to_string() in visited_states:
                #print("already seen " + state.to_string())
                state = visited_states[state.to_string()]
                state.visited = True
            else:
                visited_states[state.to_string()] = state

            if state.visited == False:
                state.visited = True
                state.g = state.get_distance(s.position) + s.g
                h = state.get_heuristic()
                priority = state.g + h
                state.parent = s
                #print('unvisited. priority = ' + str(priority) + str(state.position))
                state.priority = priority
                #print('state: ' + state.to_string() + ' parent: ' + s.to_string())
                pq.put(state)

            # if visited
            else:
                #print("visited: comparing values " + str(state.get_distance(s.position) + s.g) + ' ' + str(state.g))
                if state.get_distance(s.position) + s.g < state.g:
                    state.g = state.g + state.get_distance(s.position)
                    h = state.get_heuristic()
                    priority = state.g + h
                    state.priority = priority
                    state.parent = s
                    #print('parent updated state: ' + state.to_string() + ' parent: ' + s.to_string())
                    #print(str(priority) + str(state.position))
                    pq.put(state)

        #print("here")
        s = pq.get()

    return s

# calls an action based on two states
def action(prev, current):
    # stringify for comparison
    prevstr = prev.to_string()
    curstr = current.to_string()

    # break apart at the colon
    prev_chunks = prevstr.split(':')
    cur_chunks = curstr.split(':')

    # check if positions are diff
    if (prev_chunks[0] != cur_chunks[0]):
        print('driving ' + cur_chunks[0])
        map = Map()
        map.e = cur_chunks[0]
        map.drive()
        return

    # next break up the dicts and check individually
    prev_bal = prev.balloons
    cur_bal = current.balloons

    # check if any key has changed - if so, call pickup / putdown accordingly
    for key in prev_bal:
        if prev_bal[key] != cur_bal[key]:
            # check if pick up or put down
            if prev_bal[key] == None:
                print('putting down ' + key)
            else:
                print('picking up ' + key)
#                d = Driver()
#                d.pickup(key)

# read in file name
r = robot()
pose = r.getMCLPose()

with open('start.json') as f1:
    start = json.load(f1)

with open('simple.json') as f1:
    goal = json.load(f1)

# start and end state, nodelist
#balloons = { 'B': (7,4), 'A': (10, 10), 'C': (100,100) }
#goal_balloons = { 'B': (3,3), 'A': (5,5), 'C': (50,50) }

goal = State ( (pose[0],pose[1]),  start, None, None)
start = State( (pose[0],pose[1]), goal, goal, None)

print(start)
# goal = State ( (0,0),  goal, None, None)
# start = State( (0,0), start, goal, None)
s = aStar(start)

# trace the path
path = [s]
while (s != None):
    path.append(s)
    s = s.parent

# print all the states
path.reverse()
prev_state = path[0]
path.remove(prev_state)

# init ryan's driver
for state in path:
    # call an action, and update prev_state
    # print(prev_state.to_string() + ' ' + state.to_string())
    action(prev_state, state)
    prev_state = state

print('putting down final balloon')

# for state in path:
#     print(state.to_string())

# a star
