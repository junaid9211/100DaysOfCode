from turtle import Turtle, Screen

# draw square

turtle = Turtle()
turtle.shape('turtle')

for _ in range(4):
    turtle.right(90)
    turtle.forward(100)

screen = Screen()
screen.exitonclick()