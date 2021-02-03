class Wing(object):

    def __init__(self, ratio): #thrust/weight ratio
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print('Whee, this is fun.')
        elif self.ratio == 1:
            print('This is hard, but I\'m flying.')
        else:
            print('I think I\'ll just walk.')

class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print('Waddle, waddle, waddle.')

    def swim(self):
        print('Come on in, the water\'s lovely.')

    def quack(self):
        print('Quack quack.')

    def fly(self):
        self._wing.fly()

class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print('Come on in, but it\'s a bit chilly far South.')

    # def quackr(self):
    #     print("Are you 'avin a larf? I'm a penguin!")

    def quack(self):
        print("Are you 'avin a larf? I'm a penguin!")

def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == '__main__':
    donald = Duck()
    donald.fly() # Duck has a wing object, Duck is composed of wing.
