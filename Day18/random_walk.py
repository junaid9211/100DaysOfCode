from turtle import Turtle, Screen
import turtle as t
import random
# draw a random path
t.colormode(255)
tim = Turtle()
tim.pensize(13)
tim.speed(10)

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for _ in range(1000):
    tim.forward(30)
    tim.color(random_color())
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
