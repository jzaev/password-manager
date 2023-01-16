from tkinter import *
from tkinter import messagebox
import random
import pyperclip


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

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    site_data = site_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    if len(site_data) * len(email_data) * len(password_data) == 0:
        messagebox.showerror(title="not filled", message="Fill all fields to save your password.")
        return

    save_ok = messagebox.askquestion(title="Check your data", message=f"Site: {site_data} \n"
                                                                      f"email: {email_data}\n"
                                                                      f"pass:{password_data}\n"
                                                                      f"save this data?")

    if save_ok == "no":
        return

    with open("passwords.dat", mode="a") as data_file:
        data_string = f"{site_data} | {email_data} | {password_data} \n"
        data_file.write(data_string)
        site_entry.delete(0, END)
        password_entry.delete(0, END)


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

generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=add_password, width=36)
add_button.grid(column=1, row=4, columnspan=2)

site_entry = Entry(width=35)
site_entry.grid(column=1, row=1, columnspan=2)
# TODO delete insert
site_entry.insert(0, "juryzaev.com")

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "juryzaev@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
# TODO delete insert
password_entry.insert(0, "myPass")

window.mainloop()
