from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= 'Make your bet', prompt="Which turtle will win the race? \n"
                                                           "Your options are 'red', 'orange', 'yellow', 'green', 'blue', 'purple'\n"
                                                           "Enter a color: ")

is_race_on = False

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

# put the turtles on starting line
y_position = -70
for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-230, y_position)
    y_position += 30
    turtles.append(new_turtle)

# code for the turtles to race
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:

        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        turtle_position = turtle.xcor()

        if turtle_position >= 220:
            is_race_on = False
            winner_color = turtle.pencolor()

if user_bet == winner_color:
    print(f'You won!, {winner_color} is the winner')
else:
    print(f'You lost!, {winner_color} is the winner')

screen.exitonclick()
