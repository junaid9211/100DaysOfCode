from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
tim = Turtle()


# draw a spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.speed('fastest')


def draw_spirograph(radius, size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(150, 5)


screen = Screen()
screen.exitonclick()
