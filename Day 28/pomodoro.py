from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    global reps
    reps = 0
    title_label.config(text='Timer', fg=GREEN)
    ticks_label.config(text='')
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')

# ------------------------------------------ start timer ----------------------------------------------

def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    # work_secs = 10
    # short_break_secs = 5
    # long_break_secs = 8
    
    if reps % 8 == 0:
        title_label.config(text='Break', fg=RED)
        counter(long_break_secs)
    elif reps % 2 == 0:
        title_label.config(text='Break', fg=PINK)
        counter(short_break_secs)
    else:
        title_label.config(text='Work', fg=GREEN)
        counter(work_secs)



#  ---------------------------------------- Counter Mechanism ------------------------------------
def counter(count):
    global timer
    minutes = count // 60
    seconds = count % 60
    minutes_text = "{:02d}".format(minutes)
    seconds_text = "{:02d}".format(seconds)

    canvas.itemconfig(timer_text, text=f'{minutes_text}:{seconds_text}')
    if count > 0:
        timer = window.after(1000, counter, count-1)
    else:
        start_timer()
        ticks = reps // 2
        ticks_label.config(text='✔'*ticks)


# ------------------------------------------- Create UI ----------------------------------------
window = Tk()
window.title('Pomodoro')
window.minsize(width=300, height=100)
window.config(padx=20, pady=50, bg=YELLOW)


title_label = Label(text='Timer', font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 110, image=tomato)
timer_text = canvas.create_text(100, 125, text='00:00', fill='white', font=(FONT_NAME, 37, 'bold'))
canvas.grid(row=1, column=1)

start_btn = Button(text='Start', padx=10, pady=5, font=(FONT_NAME, 15, 'bold'), command=start_timer)
start_btn.grid(row=2, column=0, sticky=E)

reset_btn = Button(text='reset', padx=10, pady=5, font=(FONT_NAME, 15, 'bold'), command=reset_timer)
reset_btn.grid(row=2, column=2, sticky=W)

ticks_label = Label(font=(FONT_NAME, 15, 'bold'), fg=GREEN, bg=YELLOW)
ticks_label.grid(row=3, column=1)

window.mainloop()