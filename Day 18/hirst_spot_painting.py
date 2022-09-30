import turtle as t
import random

colors = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64),
          (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58),
          (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216),
          (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179), (122, 169, 190),
          (29, 85, 93), (228, 175, 166), (181, 190, 206), (67, 77, 36), (8, 243, 241)]

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.speed('fastest')
tim.hideturtle()


def draw_dots(num_of_dots, dot_size, distance):
    for _ in range(num_of_dots):
        color = random.choice(colors)
        tim.dot(dot_size, color)
        tim.forward(distance)


x_position = -250
y_position = -230
dot_lines = 10
for _ in range(dot_lines):
    tim.goto(x_position, y_position)
    draw_dots(num_of_dots=10, dot_size=20, distance=50)
    y_position += 50


screen = t.Screen()
screen.exitonclick()
