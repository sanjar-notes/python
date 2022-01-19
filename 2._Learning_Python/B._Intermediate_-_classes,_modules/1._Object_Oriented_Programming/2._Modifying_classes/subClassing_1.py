# class Kettle(object):

#     def __init__(self, make, price):
#         self.make = make
#         self.price = price
#         self.on = False

#     def intro(self):
#         for i in self.__dict__.items():
#             print(i[0], ':', i[1])


#     def switch(self):
#         self.on = not self.on

# kenwood = Kettle('Kenwood', 8.99)
# hamilton = Kettle('Hamilton', 14.55)

# kenwood.power_source = 2    # subclassing a data-attribute to the kenwood object

# kenwood.intro()
# print('-'*20)
# hamilton.intro()    # power source not added here
# print(hamilton.power_source) # it is false
print('Hello, World!!')

