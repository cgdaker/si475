class State:

    # takes in a position and a disctionary of balloon locations
    def __init__(self, position, balloons, nodelist):
        self.position = position
        self.balloons = balloons
        self.nodes = nodelist
        
    # returns list of all possible states
    def get_possible_states(self):

        # list to return
        to_return = []

        # find all other positions can go to
