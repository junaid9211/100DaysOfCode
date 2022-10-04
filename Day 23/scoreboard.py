from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-285, 260)
        self.update_level()


    def update_level(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.home()
        self.write('Game Over', align='center', font=FONT)



