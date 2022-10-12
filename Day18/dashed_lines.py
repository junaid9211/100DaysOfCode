from turtle import Turtle
import random

# draw dashed lines
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown', 'pink', 'black', 'cyan', 'grey']
tim = Turtle()
tim.penup()
tim.goto(-330, 270)
tim.pensize(3)
change_direction = True
tim.pendown()


for _ in range(18):
    tim.color(random.choice(colors))
    for _ in range(33):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

    if change_direction:
        tim.penup()
        tim.right(90)
        tim.forward(30)
        tim.right(90)
        change_direction = False
    else:
        tim.penup()
        tim.left(90)
        tim.forward(30)
        tim.left(90)
        change_direction = True

    tim.pendown()

