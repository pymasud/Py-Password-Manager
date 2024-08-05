from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    gen_passwd = "".join(password_list)
    pass_input.insert(0, gen_passwd)
    gen_passwd = ""
    pyperclip.copy(gen_passwd)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_input.get()
    name = name_input.get()
    passwd = pass_input.get()
    if len(web) == 0 or len(name) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {name}"f""
                                                          f"\nPassword: {passwd} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{web} | {name} | {passwd} \n")
            web_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

web_title = Label(text="Website:")
web_title.grid(row=1, column=0)
name_title = Label(text="Email/Username:")
name_title.grid(row=2, column=0)
pass_title = Label(text="Password:")
pass_title.grid(row=3, column=0)

web_input = Entry(width=35)
web_input.grid(row=1, column=1)
web_input.focus()

name_input = Entry(width=35)
name_input.grid(row=2, column=1)
name_input.insert(0, "Masudkhanv@gmail.com")

pass_input = Entry(width=21)
pass_input.grid(row=3, column=1)


genpass_title = Button(text="Generate Password", command=gen_pass)
genpass_title.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1)

window.mainloop()
