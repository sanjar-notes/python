#simple implementation of kettle

class Kettle(object):

    def __init__(self, x, y): # these are irrepective of the data members
        self.make = x
        self.price = y
        self.on = False

    def intro(self):
        print(repr(self))
kenwood = Kettle('Kenwood', 8.99)
hamilton = Kettle('Hamilton', 14.55)

print('Model: {0.make} = {0.price}'.format(kenwood))
