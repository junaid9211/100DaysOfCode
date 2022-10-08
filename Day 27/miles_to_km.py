from tkinter import *

def calc_km():
    # if miles_input.get().isnumeric():
    miles = float(miles_input.get())
    km = round(miles * 1.60934, 2)
    converted_km.config(text=str(km))


window = Tk()
window.title('Miles to Kilometers converter')
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

padding = {'padx': 2, 'pady': 2}

miles_input = Entry(width=15)
miles_input.grid(row=0, column=1, **padding)
miles_input.focus()

miles_label = Label(text='Miles')
miles_label.grid(row=0, column=2, **padding)

km_label = Label(text='Km')
km_label.grid(row=1, column=2, **padding)

is_equal = Label(text='is equal to')
is_equal.grid(row=1, column=0, **padding)

converted_km = Label(text='0')
converted_km.grid(row=1, column=1, **padding)

calc_button = Button(text='calculate', command=calc_km)
calc_button.grid(column=1, row=2, **padding)

window.mainloop()
