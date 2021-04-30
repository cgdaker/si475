from state import State
from queue import PriorityQueue

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

# start and end state, nodelist
balloons = { 'B': (7,4), 'A': (10, 10), 'C': (100,100) }
goal_balloons = { 'B': (3,3), 'A': (5,5), 'C': (50,50) }

goal = State ( (0,0),  goal_balloons, None, None)
start = State( (3,3), balloons, goal, None)
s = aStar(start)

# trace the path
path = [s]
while (s != None):
    path.append(s)
    s = s.parent

for state in path:
    print(state.to_string())


# for state in path:
#     print(state.to_string())

# a star
