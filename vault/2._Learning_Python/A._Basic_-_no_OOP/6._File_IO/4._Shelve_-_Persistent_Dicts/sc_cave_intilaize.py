# creates the persistent dicts
# locations = {'0': {"desc": "You are sitting in front of a computer learning Python",
#                  "exits": {},
#                  "namedExits": {}},
#              '1': {"desc": "You are standing at the end of a road before a small brick building",
#                  "exits": {"W": '2', "E": '3', "N": '5', "S": '4', "Q": '0'},
#                  "namedExits": {"2": '2', "3": '3', "5": '5', "4": '4'}},
#              '2': {"desc": "You are at the top of a hill",
#                  "exits": {"N": '5', "Q": '0'},
#                  "namedExits": {"5": '5'}},
#              '3': {"desc": "You are inside a building, a well house for a small stream",
#                  "exits": {"W": '1', "Q": '0'},
#                  "namedExits": {"1": '1'}},
#              '4': {"desc": "You are in a valley beside a stream",
#                  "exits": {"N": '1', "W": '2', "Q": '0'},
#                  "namedExits": {"1": '1', "2": '2'}},
#              '5': {"desc": "You are in the forest",
#                  "exits": {"W": '2', "S": '1', "Q": '0'},
#                  "namedExits": {"2": '2', "1": '1'}}
#              }

# vocabulary = {"QUIT": "Q",
#               "NORTH": "N",
#               "SOUTH": "S",
#               "EAST": "E",
#               "WEST": "W",
#               "ROAD": "1",
#               "HILL": "2",
#               "BUILDING": "3",
#               "VALLEY": "4",
#               "FOREST": "5"}
import shelve

with shelve.open('locations_p') as locations_p:
    for key in locations_p:
        print(key, locations_p[key])
print('\n'+'#'*40)
with shelve.open('vocabulary') as vocabulary_p:
    for key in vocabulary_p:
        print(key, vocabulary_p[key])

