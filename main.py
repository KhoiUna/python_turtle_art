import turtle
from math import sqrt
from draw_stair import draw_stair
from draw_sun import draw_sun
from random import *


def main():
    # Declare stairway's properties
    steps = 15
    length = steps * 140/9
    height = (length / 3)
    diagonal_length = length / 9 * sqrt(2)

    # Declare my_turtle
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.goto(-length / 2, -270)
    my_turtle.pendown()

    circle_radius = 0
    circle_down = 0
    bg_color = 'black'
    # Draw stairway
    for i in range(0, steps):
        if i > 3:
            circle_down += height
        if i == 7:
            circle_radius = length * 2

        screen = turtle.Screen()
        screen.bgcolor(bg_color)
        length = draw_stair(my_turtle, length, height, diagonal_length)
        height = (length / 3)
        diagonal_length = length / 9 * sqrt(2)
        # Change background color
        if bg_color == 'black':
            bg_color = 'white'
        else:
            bg_color = 'black'

    # Finish the last stair
    my_turtle.forward(length)
    my_turtle.right(90)

    # Draw the sun
    draw_sun(my_turtle, circle_radius)

    turtle.exitonclick()


if __name__ == '__main__':
    main()
