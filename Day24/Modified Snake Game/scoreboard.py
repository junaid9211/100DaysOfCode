from turtle import Turtle
import turtle

ALIGNMENT = 'center'
SCORE_FONT = ('Consolas', 23, 'normal')
LEVEL_FONT = ('Consolas', 15, 'normal')
FILE_NAME = 'high_score.txt'
turtle.colormode(255)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.current_level = 1
        self.highscore = self.get_highscore()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f'Score: {self.score} High score: {self.highscore}', align=ALIGNMENT, font=SCORE_FONT)
        self.goto(-380, 270)
        self.write(f'Level: {self.current_level}', align='left', font=LEVEL_FONT)



    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(FILE_NAME, mode='w') as f:
                f.write(str(self.highscore))

        self.score = 0
        self.current_level = 1
        self.update_scoreboard()


    def get_highscore(self):
        try:
            with open(FILE_NAME) as f:
                contents = int(f.read())
        except:
            with open(FILE_NAME, mode='w') as f:
                f.write('0')
                contents = 0

        return contents



