from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Calibre", 10, "normal")


# ---------------------PASSWORD GENERATOR ----------------
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)  # Clears the entry
    password_entry.insert(0, password)  # Shows random pass into the entry
    pyperclip.copy(password)  # Copies the random pass into clipboard


# ---------------------SAVE PASSWORD----------------------
def save():
    web_details = web_entry.get()
    email_details = email_entry.get()
    password_details = password_entry.get()
    new_data = {
        web_details: {
            "email": email_details,
            "password": password_details,
        }
    }

    if len(web_details) == 0 or len(email_details) == 0 or len(password_details) == 0:
        messagebox.showerror(message="Please don't leave any field empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the json data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating the data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Writing the data into existing data
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)

        # is_ok = messagebox.askokcancel(title=f"{web_details}", message=f"These are the info entered:"
        #                                                                f"\nEmail: {email_details}"
        #                                                                f"\nPassword: {password_details}"
        #                                                                f"\nIs it ok to save?")
        # if is_ok:
        #     with open("text.txt", "a") as data:
        #         data.write(f"{web_details} | {email_details} | {password_details} \n")
        #         web_entry.delete(0, END)
        #         # email_entry.delete(0, END)
        #         password_entry.delete(0, END)


# ---------------------SEARCH PASSWORD --------------------------
def find_password():
    with open("data.json", "r") as data_file:
        web_details = web_entry.get()
        # Reading the json data
        data = json.load(data_file)
        if web_details in data:
            messagebox.showinfo(title=f"{web_details}", message=f"Email: {data[f'{web_details}']['email']}\n"
                                                                f"Password: {data[f'{web_details}']['password']}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists")


# ------------------------UI SETUP -------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=50)

canvas = Canvas(height=200, width=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(123, 100, image=lock_image)
canvas.grid(row=0, column=1, pady=20)

# ------------------------FORM------------------------------
web_name = Label()
web_name.config(text="Website:", font=FONT)
web_name.grid(row=1, column=0)

web_entry = Entry()
web_entry.config(width=37)
web_entry.grid(row=1, column=1, pady=5)
web_entry.focus()

email_name = Label()
email_name.config(text="Email/Username:", font=FONT)
email_name.grid(row=2, column=0)

email_entry = Entry()
email_entry.config(width=58)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "@gmail.com")

password_name = Label()
password_name.config(text="Password:", font=FONT)
password_name.grid(row=3, column=0)

password_entry = Entry()
password_entry.config(width=37)
password_entry.grid(row=3, column=1, pady=5)

password_gen_button = Button()
password_gen_button.config(text="Generate Password", font=FONT, height=1, command=generate_password)
password_gen_button.grid(row=3, column=2, pady=5)

search_button = Button()
search_button.config(text="Search", font=FONT, height=1,width=15, command=find_password)
search_button.grid(row=1, column=2, pady=5)

add_button = Button()
add_button.config(text="Add", font=FONT, height=1, width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
