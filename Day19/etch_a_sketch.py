import turtle as t
import random

# you can control the turtle using keyboard and make drawings
# Functions
# w: move forward, s: move backward, a: turn left, d: turn right
# c: clear screen, j: draw a dot, k: change color, l: toggle pen on or off

colors = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64),
          (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58),
          (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216),
          (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179), (122, 169, 190),
          (29, 85, 93), (228, 175, 166), (181, 190, 206), (67, 77, 36), (8, 243, 241)]

t.colormode(255)
tim = t.Turtle()
tim.pensize(4)
screen = t.Screen()
pen_down = True


def toggle_pen():
    global pen_down
    if pen_down:
        tim.penup()
        pen_down = False
    else:
        tim.pendown()
        pen_down = True


def draw_dot():
    tim.dot(20)


def change_color():
    tim.color(random.choice(colors))


def clear_screen():
    tim.clear()
    tim.color('black')
    tim.penup()
    tim.home()
    tim.pendown()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(8)


def turn_right():
    tim.right(8)


screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='c', fun=clear_screen)
screen.onkeypress(key='j', fun=draw_dot)
screen.onkeypress(key='k', fun=change_color)
screen.onkeypress(key='l', fun=toggle_pen)

# draw dots,
# change color
# increase, decrease width
# pen up, pen down
screen.exitonclick()
