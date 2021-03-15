class Player():
    """Player info"""

    def __init__(self, name='New Player'):
        self.name = name
        self._lives = 3
        self.level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print('Lives can\'t be negative')
            self._lives = 0

    lives = property(_get_lives, _set_lives, doc="power")
    # printing the variables
    def __str__(self):
        return "Names: {0.name}, Lives: {0._lives}, Level: {0.level}, Score: {0.score}".format(self)

if __name__ == '__main__':
    print('')
