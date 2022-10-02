from turtle import Turtle
import random
import turtle

turtle.colormode(255)


class Food(Turtle):
    def __init__(self, color, xlim, ylim):
        super().__init__()
        self.color_name = color
        self.xlim = xlim
        self.ylim = ylim
        self.penup()
        self.color(self.color_name)
        self.shape('circle')
        self.speed('fastest')
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.refresh()


    def refresh(self):
        new_x = random.randint(self.xlim[0], self.xlim[1])
        new_y = random.randint(self.ylim[0], self.ylim[1])
        self.goto(new_x, new_y)
