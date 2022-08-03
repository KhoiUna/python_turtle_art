import turtle
from math import sqrt
from draw_stair import draw_stair
from draw_sun import draw_sun
from random import *


def main():
    steps = int(input("How many steps do you want to draw? "))
    want_to_draw_sun = input("Do you want to see the sun? (y/n) ")

    screen = turtle.Screen()
    screen.bgcolor('black')

    # Declare stairway's properties
    # These ratios keep the stairway's proportions
    LENGTH_RATIO = 140/9
    HEIGHT_RATIO = 1/3
    DIAGONAL_LENGTH_RATIO = 1/9 * sqrt(2)

    length = steps * LENGTH_RATIO
    height = length * HEIGHT_RATIO
    diagonal_length = length * DIAGONAL_LENGTH_RATIO

    # Declare my_turtle
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.goto(-length / 2, -270)
    my_turtle.pendown()

    circle_radius = 0
    circle_down = 0
    # Draw stairway
    for i in range(0, steps):
        # 
        if i > 3:
            circle_down += height
        if i == 7:
            circle_radius = length * 2
        
        length = draw_stair(my_turtle, length, height, diagonal_length)
        height = (length / 3)
        diagonal_length = length / 9 * sqrt(2)       

    # Finish the last stair
    my_turtle.forward(length)
    my_turtle.right(90)

    # Draw the sun
    if(want_to_draw_sun == 'y'):
        draw_sun(my_turtle, circle_radius)

    turtle.exitonclick()


if __name__ == '__main__':
    main()
