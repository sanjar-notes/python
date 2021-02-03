class Enemy(object):
    """An abstract class - We'll let the type be just the name"""
    def __init__(self, name='Enemy', hit_points=0, lives=1):
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
    pass

if __name__ =='__main__':
    from player import Player

    # tim = Player('Tim')

    # random_monster = Enemy('Basic Enemy', 12, 1)
    # print(random_monster)

    # random_monster.take_damage(12.5)
    # print(random_monster)

    ugly_troll = Troll() # we specified any Troll
    print('Ugly troll - {}'.format(ugly_troll))

    another_troll = Troll("Ug", 18, 1)
    print('Another troll - {}'.format(another_troll))

    brother = Troll("Urg", 23, 1)
    print('Another troll - {}'.format(another_troll))
