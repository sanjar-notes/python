import pickle
p1 = ('Power Rangers', 'Ninja Storm', 3, 2002)
p2 = ('Power Rangers', 'Dino Thunder', 3, 2003)
with open('pickly', 'bw') as pickle_file:
    pickle.dump(p1, pickle_file)
    pickle.dump(p2, pickle_file)

with open('pickly', 'br') as pickle_file:
    # pickle.load(pickle_file)
    print(pickle.load_data(pickle_file))
    # print(pickle.load(pickle_file))

