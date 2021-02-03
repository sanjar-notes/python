color = 'Global color'

class Car:
    # Car.color = 'Static color' - # Error, Car.color does not exist
    color = 'Static color' # Correct declaration

    def __init__(self):
        pass

    def printColor(self):
        print(color) # global color
        print(Car.color) # static color

    #static function - cannot be called by Car objects
    @staticmethod
    def static_func():
        print('Inside a static func')

    # inner class or static class
    class Wheel():
        def __init__(self):
            print('Inside Car.Wheel')
            pass


if __name__ == "__main__":
    c = Car()
    c.printColor()

    Car.static_func() # access static method w/o object
    c.static_func() # static method call with object

    w = Car.Wheel()
