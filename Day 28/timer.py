from tkinter import *

BLACK = '#181818'
timer = None
timer_running = False

window = Tk()
window.title('Timer')
window.maxsize(width=200, height=120)
window.minsize(width=200, height=120)
window.config(padx=10, pady=10, bg=BLACK)


def reset_timer():
    window.after_cancel(timer)
    time_text.config(text='00:00')
    start_btn.config(text='Start')

def start_timer():
    time = time_entry.get()
    if time == '':
        reset_timer()
    elif time.isdigit():
        if timer_running:
            reset_timer()

        seconds = int(time) * 60
        time_entry.delete(0, END)
        counter(seconds)


def counter(count):
    global timer
    global timer_running
    timer_running = True
    minutes = count // 60
    seconds = count % 60
    minutes_text = "{:02d}".format(minutes)
    seconds_text = "{:02d}".format(seconds)
    time_text.config(text=f'{minutes_text}:{seconds_text}')
    if count > 0:
        timer = window.after(1000, counter, count-1)
        start_btn.config(text='Reset')
    else:
        timer_running = False
        start_btn.config(text='Start')


input_label = Label(text='Mins', fg='white', bg=BLACK, font=('Ariel', 10, 'normal'))
input_label.grid(row=0, column=0)

time_entry = Entry(width=3, font=('Ariel', 15, 'normal'))
time_entry.grid(row=0, column=1)
time_entry.focus()

start_btn = Button(text='Start', font=('Ariel', 10, 'normal'), command=start_timer, bg='#ffffff')
start_btn.grid(row=0, column=2)

time_text = Label(text='00:00', font=('Ariel', 50, 'normal'), fg='white', bg=BLACK)
time_text.grid(row=1, column=0, columnspan=3)

window.mainloop()