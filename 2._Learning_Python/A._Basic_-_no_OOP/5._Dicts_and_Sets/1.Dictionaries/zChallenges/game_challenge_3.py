
# Game challenge

# we use hash tables for making the automaton
# '''
places = {
        0:"Your Room",
        1: "Road",
        2: "Hill",
        3: "Building",
        4: "Valley",
        5: "Forest"
}

# N S E W are the moves possible from each location
maze = {
        1: {"N": 5, "S": 4, "E": 3, "W": 2},
        2: {"N": 5},
        3: {"W": 1},
        4: {"N": 1, "W": 2},
        5: {"W": 2, "S":1 }
}

# we need to make west synonymous with W, west, go west, turn west etc.
# east with E, east, go east, move to east - but not west
# north, N , North
# south

# solution, if we have any word which has the initial letter as N, S, E, W we are good to go.
# we'll split and check
# we only need words of length 1 or 4 or 5
# THE FUNCTION

import os
os.system('clear')

def getDirection(entered):
    # remove the whitespaces
    keywords = entered.split()
    for i in keywords:
        i = i.upper()
        if i in ['Q', 'EXIT', 'QUIT', 'END', 'OVER', 'END', 'BYE']:
                return 'Q'
        if len(i) == 1 or 3 < len(i) < 6:
            if i[0] in 'NSEW':
                return i[0]

curr = 1  #in our room
print('Starting from:', places[curr])
while True:
    availableMoves = maze[curr].keys()
    print('Available Moves:', ', '.join(availableMoves)+', Q')
    move = getDirection(input('Move: '))
    if move == 'Q':
        print('Game Over, you have finally reached the', places[curr], '\b.')
        break
    elif move in availableMoves:
        curr = maze[curr][move]
        print('You are at: ', places[curr])
    else:
        print('Path does not exist...')
