from state import State

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

# start and end state, nodelist
path = 'file.txt'
nodelist = get_nodelist(path)
init_state = State((0,0), {"B": (1,1) }, nodelist)
end = State((0,0) {"B": (2,2)}, nodelist)

# a star
