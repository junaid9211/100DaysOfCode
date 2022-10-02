from turtle import Turtle
import turtle
ALIGNMENT = 'center'
FONT = ('Consolas', 26, 'normal')

turtle.colormode(255)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write('Game Over', align=ALIGNMENT, font=FONT)
