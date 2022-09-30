import random
from turtle import Turtle, Screen

# draw polygons


def draw_shape(sides):
    angle = 360/sides
    for _ in range(sides):
        tim.forward(130)
        tim.right(angle)


colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown', 'pink', 'black', 'cyan', 'grey']
tim = Turtle()
tim.penup()
tim.goto(-100, 150)
tim.pendown()


for sides in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(sides)

screen = Screen()
screen.exitonclick()