from player import Player

tim = Player('Tim')
print(tim.name)
print(tim.lives)

tim.lives -= 1
print(tim)

# for i in range(3):
#     print('-'*20)
#     tim.lives -= 1
#     print(tim)
print(tim.__str__())
