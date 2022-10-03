from turtle import Turtle
import turtle

turtle.colormode(255)


class Ball(Turtle):
    def __init__(self, color):
        super().__init__()
        self.x_move = 4
        self.y_move = 4
        self.move_speed = 0.01
        self.color(color)
        self.shape('circle')
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1


    def reset_position(self):
        self.bounce_x()
        self.home()



