from turtle import *

done = "Well done, you have finished your drawing"
forward(150)
right(250)
forward(150)
circle(75)

done()

# print(done)


# 1 + 3k(one offset)
def spiral(n, a):
    up()
    forward(a)
    n = n - 1
    right()
    for i in range(0, n, 3):
        forward(a)
        down()
        forward(a)
        left()
        forward(a)
