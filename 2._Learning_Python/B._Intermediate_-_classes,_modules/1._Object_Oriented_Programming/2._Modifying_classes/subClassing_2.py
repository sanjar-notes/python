class Kettle(object):

    power = 'Atomic' # ~ a static variable
    count = 0

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def intro(self):
        for i in self.__dict__.items():
            print(i[0], '\b:', i[1])
        print('Static power:', self.power)

    def switch(self):
        self.on = not self.on


kenwood = Kettle('Kenwood', 8.99)
hamilton = Kettle('Hamilton', 14.55)

# we make a subclass variable, for kenwood
kenwood.power = 'Overshadowed'   # overshadows the power class(static) variable, both outside and inside the class
# # 1 overshadowing is a problem
# print(kenwood.power)   # accesses the instance variable, static variable is out of scope
# print(hamilton.power)  # accesses the static variable power


# # 2 is a new attribute created, if names are the same? - Yes. Also static methods and variables cannot be accessed by instances
# Kettle.power = 'Atomic'    # assigns to the static variable, proves that a new variable is created for kenwood
# print('kenwood', (kenwood.__dict__))
# print('-'*20)
# print('hamilton', (hamilton.__dict__))
