class State:

    # takes in a position and a disctionary of balloon locations
    def __init__(self, position, balloons, goal, parent, priority=1000):
        self.position = position
        self.balloons = balloons
        self.goal = goal
        self.parent = parent
        self.visited = False
        self.g = 0
        self.priority = priority

    # returns list of all possible states
    def get_possible_states(self):

        # list to return
        to_return = []
        near_balloons = {}

        for state in self.drive_to():
            #print(state.to_string())
            to_return.append(state)

        #print(self.to_string())

        for state in self.pick_up():
            #print(state.to_string())
            to_return.append(state)

        for state in self.put_down():
            #print(state.to_string())
            to_return.append(state)

        return to_return


    def put_down(self):
        to_return = []

        # check if near enough goal location to put down
        for key in self.goal.balloons:
            if self.get_distance(self.goal.balloons[key]) < 1:
                put_down = self.balloons.copy()
                put_down[key] = self.position
                ret = State(self.position, put_down, self.goal, self)
                #print(ret.to_string())
                to_return.append(ret)

        return to_return


    def drive_to(self):
        to_return = []
        # find all other positions can go to
        for key in self.balloons:
            if (self.balloons[key] == None):
                continue

            if (self.get_distance(self.balloons[key]) < .5):
                continue

            toreturn = State(self.balloons[key], self.balloons, self.goal, self)
            #print(toreturn.to_string())
            to_return.append(toreturn)
        return to_return

    def to_string(self):
        return str(self.position) + ' ' + str(self.balloons)

    def pick_up(self):
        to_return = []

        # check if space to pick up
        count = 0
        for key in self.balloons:
            if self.balloons[key] == None:
                count += 1

        # if greater than one skip
        if count < 2:

            # check if near a balloon to pick up
            for key in self.balloons:

                if (self.balloons[key] == None):
                    continue

                # check if can pick up
                if self.get_distance(self.balloons[key]) < 1:

                    # set position of balloon to none to show its being carried
                    pick_up = self.balloons.copy()
                    pick_up[key] = None
                    ret = State(self.position, pick_up, self.goal, self)
                    #print(ret.to_string())
                    to_return.append(ret)

        return to_return

    def __lt__(self, other):
        return self.priority < other.priority

    # returns distance from goal state
    # returns -1 if this is goal state
    def get_heuristic(self):
        # get total distance from each balloon to ideal balloon
        total = 0
        for key in self.balloons:
            current = self.balloons[key]
            goal = self.goal.balloons[key]

            # check if already being carried
            if current == None:
                current = self.position

            diff = (current[0] - goal[0]) ** 2
            diff += (current[1] - goal[1]) ** 2
            diff = (diff ** .5) / 2

            total += diff

        if total < .5:
            return -1
        return total

    # returns distance between two states
    def get_distance(self, position):
        to_return = (self.position[0] - position[0]) ** 2
        to_return += (self.position[1] - position[1]) ** 2
        return to_return ** .5



# balloons = { 'B': None, 'A': (10, 10), 'C': (100,100) }
# goal_balloons = { 'B': (3,3), 'A': (5,5), 'C': (50,50) }
# #
# goal = State ( (0,0),  goal_balloons, None, None)
# start = State( (3,3), balloons, goal, None)
# for state in start.get_possible_states():
#     print(state.position)
#     print(state.balloons)
#     print('\n')
