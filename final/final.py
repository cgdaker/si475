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

    s = root
    # -1 indicates this is goal state
    while (s.get_heuristic() != -1):
        print(str(s.position) + ' ' + str(s.balloons))
        # get list of all adjacent states
        adj_states = s.get_possible_states()

        # remove current state
        for state in adj_states:
            if state.position == s.position and state.balloons == s.balloons:
                print('removed')
                adj_states.remove(state)


        for state in adj_states:
            print(str(state.position) + ' ' + str(state.balloons))
            if state.visited == False:
                print("in unvisited")
                state.g = state.get_distance(s.position)
                h = state.get_heuristic()
                priority = state.g + h
                print(str(priority) + str(state.position))
                state.priority = priority
                pq.put(state)

            # if visited
            else:
                print("visited")
                if (state in pq) and state.get_distance(s.position) + state.g < state.g:
                    state.g = state.g + state.get_distance(s.position)
                    h = state.get_heuristic()
                    priority = state.g + h
                    state.priority = priority
                    pq.put(state)

        #print("here")
        s = pq.get()
        print('\n')
        # while not pq.empty():
        #     state = pq.get()
        #     print(state.position)
        #     print(state.balloons)
        #     print('\n')
        #print(s)

# start and end state, nodelist
balloons = { 'B': (7,4), 'A': (10, 10), 'C': (100,100) }
goal_balloons = { 'B': (3,3), 'A': (5,5), 'C': (50,50) }

goal = State ( (0,0),  goal_balloons, None, None)
start = State( (3,3), balloons, goal, None)
aStar(start)

# a star
