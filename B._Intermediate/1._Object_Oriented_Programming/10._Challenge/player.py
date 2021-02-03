class Player():
    """Player info"""
    def __init__(self, name='New Player'):
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print('Lives can\'t be negative')
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        # check if _level increased by 2
        if level > 0:
            delta = level - self._level  # level drop/rise
            self.score += 1000 * delta
        else:
            print('Level should be greater or equal to 1')
            self._level = 1  # nothing happens to the score

    # triggers
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)  # challenge, we need to check the spike in level alone - need both getter and setter

    # printing the variables
    def __str__(self):
        return "Names: {0.name}, Lives: {0._lives}, Level: {0._level}, Score: {0.score}".format(
            self)


if __name__ == '__main__':
    print('')
