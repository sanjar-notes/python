class Car(object):

    @staticmethod
    def _carCount():
        # return _count
        print('Car created')

    def __init__(self, make, price, color):
        # _count+=1
        self.make = make
        self.price = price
        self.color = color
        self.__seater = 24

    def intro(self):
        print(self.make, self.price, self.color, self.__seater)

        self._Car__seater = 997 # same as below
        self.__seater = 234
    # power is great, power works it adds value 
if __name__=='__main__':
    bugati = Car('Bugati', 23, 'Blue')
    bugati.intro()
    print(bugati.__dict__)
