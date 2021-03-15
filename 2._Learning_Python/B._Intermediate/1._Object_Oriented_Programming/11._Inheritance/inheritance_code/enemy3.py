class Enemy(object):
    """An abstract class - We'll let the type be just the name"""
    def __init__(self, name='Enemy', hit_points=0, lives=1):
        print('Enemy constructor called', end='. ')
        self.name = name
        self.hit_points = hit_points    # HP
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points > 0:
            self.hit_points = remaining_points
            print('I took {} points damage, current HP = {}.'.format(damage, self.hit_points))
        else:
            self.lives -= 1
            self.hit_points = 0 #HP cannot be negative
            if self.lives == 0:
                print('I\'m dead')
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)


class Troll(Enemy):
    def __init__(self, name='Troll', lives=1, hit_points=23):
        Enemy.__init__(self, name=name, lives=1, hit_points=hit_points) # How can we pass a Troll type as self for the enemy class

    def grunt(self):
        print('Me {0}, {0} stomp you.'.format(self.name))


if __name__ =='__main__':
    ugly_troll = Troll() # we specified any Troll
    print('Ugly troll - {}'.format(ugly_troll))

    another_troll = Troll("Ug", 18, 1)
    print('Another troll - {}'.format(another_troll))

    brother = Enemy("Urg", 23)
    print('Another troll - {}'.format(brother))
    another_troll.grunt()

# __str__ is still accessible - this means that all methods are kept together, with the parent class's method given preference.
# But they are overriden if we specify the values.
# Also, self now can access all the values. There's only one self when inheriting.
