class Kettle(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumi(self):
        return self.a+self.b
    # a = property(sumi)

k = Kettle(1, 2)
Kettle.sumi(k)
print(k.a)
