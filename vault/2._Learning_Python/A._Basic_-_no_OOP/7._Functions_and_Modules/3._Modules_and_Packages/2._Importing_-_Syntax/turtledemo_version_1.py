import time
import turtle

def spiral_square(lent=20, goal=50):
    moves = 0
    while moves < goal:
        turtle.left(90)
        turtle.forward(lent)
        lent += 10
        moves += 1
    time.sleep(0.5)

def circle(radius=50, offset=10):
    moves = 0
    lent = 1
    # turtle.forward(radius)
     # we are at (radius, 0)
    while moves < 100:
        # make the circle
        arcm = radius*3.1416/180
        for i in range(360):
        # move forward take a left turn
            turtle.forward(arcm)
            turtle.left(1)
            lent += 10
        # we are at (radius, 0)
        turtle.right(90)
        turtle.forward(offset)
        # we are now at r+offset
        radius+=offset

        # lookup
        turtle.left(90)
        moves += 1

        # time.sleep(0.1)

def spiral(radiusMax=5000):
    radius = 1
    # turtle.forward(radius)
    arcm = 0
    divs = 360
    ang = 0
    # we are at (radius, 0)

    turtle.forward(radius)
    turtle.left(90)
    while radius < radiusMax:
        # make the arc
    # move forward take a left turn
        arcm +=radius*3.1416/divs
        divs+=5
        radius+=10
        ang=(ang+1)%360
        turtle.forward(arcm)
        turtle.left(ang)
        time.sleep(0.001)

spiral_square()
