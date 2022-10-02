from turtle import Turtle
import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

turtle.colormode(255)


class Snake:
    def __init__(self, color):
        self.color_name = color
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color(self.color_name)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for segment_index in range(len(self.segments)-1, 0, -1):
            new_position = self.segments[segment_index-1].position()
            self.segments[segment_index].goto(new_position)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN and self.head.heading() != UP:
            self.head.setheading(UP)
            self.move()

    def down(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(DOWN)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(LEFT)
            self.move()

    def right(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)
            self.move()



