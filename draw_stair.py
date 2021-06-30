from math import sqrt
from random import random


def draw_stair(turtle, length, height, diagonal_length):
    # Draw rectangle
    turtle.color((random(), random(), random()))
    turtle.begin_fill()

    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(180)
    turtle.forward(height)

    turtle.end_fill()

    # Draw parallelogram's diagonal sides
    turtle.right(45)
    turtle.forward(diagonal_length)
    turtle.right(180)
    turtle.forward(diagonal_length)
    turtle.left(180 - 45)
    turtle.forward(length)
    turtle.left(90 + 45)
    turtle.forward(diagonal_length)
    x1 = turtle.xcor()
    y1 = turtle.ycor()

    # Back to original position to draw rectangle
    turtle.back(diagonal_length)
    turtle.left(45)
    turtle.forward(length)
    turtle.right(90 + 45)
    turtle.forward(diagonal_length)
    turtle.right(45)

    # Return the new length
    return sqrt((turtle.xcor() - x1)**2 + (turtle.ycor() - y1))
