class State:

    # takes in a position and a disctionary of balloon locations
    def __init__(self, position, balloons, goal):
        self.position = position
        self.balloons = balloons
        self.goal = goal

    # returns list of all possible states
    def get_possible_states(self):

        # list to return
        to_return = []
        near_balloons = {}

        for state in self.drive_to():
            print(state.position)

        print('\n')
        for state in self.pick_up():
            print(state.balloons)

        for state in self.put_down():
            print(state.balloons)


    def put_down(self):
        to_return = []

        # check if near enough goal location to put down
        for key in self.goal.balloons:
            if self.get_distance(goal.balloons[key]) < 1:
                put_down = self.balloons
                put_down[key] = self.position
                to_return.append(State(self.position, put_down, self.goal))

        return to_return


    def drive_to(self):
        to_return = []
        # find all other positions can go to
        for key in self.balloons:
            if (self.balloons[key] == None):
                continue

            to_return.append(State(self.balloons[key], self.balloons, self.goal))
        return to_return

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
                    pick_up = self.balloons
                    pick_up[key] = None
                    to_return.append(State(self.position, pick_up, self.goal))

        return to_return

    # returns distance between two states
    def get_distance(self, position):
        to_return = (self.position[0] - position[0]) ** 2
        to_return += (self.position[1] - position[1]) ** 2
        return to_return ** .5



balloons = { 'B': None, 'A': (10, 10), 'C': (100,100) }
goal_balloons = { 'B': (3,3), 'A': (5,5), 'C': (50,50) }

goal = State ( (0,0),  goal_balloons, None)
start = State( (3,3), balloons, goal)
start.get_possible_states()
