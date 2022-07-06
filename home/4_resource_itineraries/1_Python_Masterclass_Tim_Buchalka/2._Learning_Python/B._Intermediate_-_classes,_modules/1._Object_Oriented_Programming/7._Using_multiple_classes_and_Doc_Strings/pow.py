class Kettle(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return self.a

    A = property(get_a)

kenwood = Kettle(1, 2)
# print(kenwood.__dict__)
print(kenwood)
