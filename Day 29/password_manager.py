from tkinter import *
from tkinter import messagebox
from random import randint, choices, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_random_pass():
    password_input.delete(0, END)
    password = gen_pass()
    pyperclip.copy(password)
    password_input.insert(END, string=password)

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)
    random_letters = choices(letters, k=nr_letters)
    random_numbers = choices(numbers, k=nr_numbers)
    random_symbols = choices(symbols, k=nr_symbols)

    password_list = random_letters + random_numbers + random_symbols
    shuffle(password_list)
    password = ''.join(password_list)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if '' in [website, email, password]:
        messagebox.showerror('Oops', "Don't leave any fields empty")
        print('Dont leave any field blank')
    else:
        # are you sure that the info is correct?
        confirmation = messagebox.askyesno('Confirmation', f'Email: {email}\nPassword: {password}\nIs this ok?')

        if confirmation:

            # save the data
            with open('data.txt', mode='a') as f:
                row = f'{website}  |  {email}  |  {password}\n'
                f.write(row)

            # clear the fields
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)

            
            

# ---------------------------- UI SETUP ------------------------------- #
# create the window
window = Tk()
window.title('Password Manager')
window.minsize(width=250, height=200)
window.config(bg='white', padx=50, pady=50)

# add the lock image
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:', bg='white')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:', bg='white')
email_label.grid(row=2, column=0)

password_label = Label(text='Password:', bg='white')
password_label.grid(row=3, column=0)

website_input = Entry(width=48, bg='#f8f8f8')
website_input.grid(row=1, column=1, columnspan=2, sticky=E)
website_input.focus()


# Inputs
email_input = Entry(width=48, bg='#f8f8f8')
email_input.grid(row=2, column=1, columnspan=2, sticky=E)

password_input = Entry(width=27, bg='#f8f8f8')
password_input.grid(row=3, column=1, sticky=E, padx=(0, 15))

# Buttons
gen_pass_btn = Button(text='Generate Password', command=get_random_pass)
gen_pass_btn.grid(row=3, column=2)

add_pass_btn = Button(text='Add', width=41, command=save_pass)
add_pass_btn.grid(row=4, column=1, columnspan=2, sticky=E)


window.mainloop()