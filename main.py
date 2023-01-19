from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_list_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_list_letters + password_list_symbols + password_list_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    site_data = site_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    new_data = {site_data: {"email": email_data, "password": password_data}}

    if len(site_data) * len(email_data) * len(password_data) == 0:
        messagebox.showerror(title="not filled", message="Fill all fields to save your password.")
        return
    try:
        with open("passwords.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("passwords.json", mode="w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("passwords.json", mode="w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        site_entry.delete(0, END)
        password_entry.delete(0, END)


def search_password():
    try:
        with open("passwords.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="No file found", message="No file found")
        return

    searching_site = site_entry.get()
    try:
        login_data = data[searching_site]
    except KeyError:
        messagebox.showerror(title="Site data was not found!", message="Site data was not found!")
        return

    password = login_data["password"]
    email = login_data["email"]
    pyperclip.copy(password)
    messagebox.showinfo(title=f"login data for {searching_site}", message=f"{email} \n{password}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50, )

canvas = Canvas(width=200, height=200, highlightthickness=3, highlightcolor="black", borderwidth=3)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
# canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=0)
#
website_label = Label(text="Website:", font=("Times New Roman", 14,))
website_label.grid(row=1, column=0)
website_label.focus()

email_label = Label(text="email/username:", font=("Times New Roman", 14,))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Times New Roman", 14,))
password_label.grid(row=3, column=0)

search_button = Button(text="Search", command=search_password, width=16)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate password", command=generate_password, width=16)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=add_password, width=36)
add_button.grid(column=1, row=4, columnspan=2)

site_entry = Entry(width=21)
site_entry.grid(column=1, row=1)

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "juryzaev@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

window.mainloop()
