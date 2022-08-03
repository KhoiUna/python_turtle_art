from math import sqrt


def draw_sun(turtle, circle_radius: float) -> None:
    turtle.width(2)
    turtle.color('yellow')

    # Move down a few steps
    turtle.penup()
    turtle.forward(circle_radius)
    turtle.left(90)
    turtle.pendown()

    # Draw a circle
    turtle.circle(circle_radius)

    # Draw sun rays
    turtle.right(37)
    for i in range(0, 8):
        turtle.forward(circle_radius * sqrt(11/18))
        turtle.left(120)
        turtle.forward(circle_radius * sqrt(11/18))
        turtle.right(75)
