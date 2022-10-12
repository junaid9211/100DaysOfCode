from turtle import Turtle
import turtle

turtle.colormode(255)


class Paddle(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)


    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

