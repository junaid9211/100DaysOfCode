import turtle
from turtle import Turtle
import pandas as pd


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

    def write_name(self, position, text):
        self.goto(position)
        self.write(text, align='center', font=('Ariel', 9, 'bold'))


    def game_over(self):
        self.goto(0, 0)
        self.color('#888888')
        self.write('Congratulations, You named all states!', align='center', font=('Ariel', 20, 'bold'))
        self.hideturtle()



SCREEN_WIDTH = 730
SCREEN_HEIGHT = 495

# set up the game window
screen = turtle.Screen()
screen.title('Name the states')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# add image in the background
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# get the states data
df = pd.read_csv('50_states.csv')
all_states = df['state'].to_list()

writer = Writer()
answered_states = []
score = 0

# until all the states are answered
while len(answered_states) < 50:
    # get the answer
    if score == 0:
        answer_state = screen.textinput(title=f'Answered {score}/50', prompt="What's the state name?").title()
    else:
        answer_state = screen.textinput(title=f'Answered {score}/50', prompt="What's another state name?").title()


    # check if the answer is valid, and it is not already answered
    if (answer_state in all_states) and (answer_state not in answered_states):
        # grab the data related to answered state from dataframe
        answer_row = df[df.state == answer_state].iloc[0]
        state = answer_row['state']
        x = int(answer_row['x'])
        y = int(answer_row['y'])
        # write the state name on the screen
        writer.write_name(position=(x, y), text=state)
        # append the answered state, and increase the score by 1
        answered_states.append(answer_state)
        score += 1


# when all the questions are answered, write 'You named all states
writer.game_over()

turtle.mainloop()
