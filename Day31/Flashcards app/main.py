from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('data/french_words.csv')
    to_learn = df.to_dict(orient='records')
else:
    to_learn = df.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_bg, image=FRONT_IMAGE)
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    flip_timer = window.after(2000, flip_card)


def flip_card():

    canvas.itemconfig(canvas_bg, image=BACK_IMAGE)
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()




# step 1. create window
window = Tk()
window.title('Flashcards program')
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

flip_timer = window.after(2000, flip_card)

# step 2. create canvas
FRONT_IMAGE = PhotoImage(file='images/card_front.png')
BACK_IMAGE = PhotoImage(file='images/card_back.png')
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

canvas_bg = canvas.create_image(400, 263, image=FRONT_IMAGE)
language = canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='trouve', font=('Ariel', 60, 'bold'))
# step 3. create buttons
tick_image = PhotoImage(file='images/right.png')
right_btn = Button(image=tick_image, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)

cross_image = PhotoImage(file='images/wrong.png')
wrong_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

next_card()

window.mainloop()


