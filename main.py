from tkinter import *
from tkinter import messagebox

FONT = ("Calibre", 10, "normal")


# ---------------------PASSWORD GENERATOR ----------------


# ---------------------SAVE PASSWORD----------------------
def save():
    web_details = web_entry.get()
    email_details = email_entry.get()
    password_details = password_entry.get()

    is_ok = messagebox.askokcancel(title=f"{web_details}", message=f"These are the info entered:"
                                                f"\nEmail: {email_details}"
                                                f"\nPassword: {password_details}"
                                                f"\nIs it ok to save?")
    if is_ok:
        with open("text.txt", "a") as data:
            data.write(f"{web_details} | {email_details} | {password_details} \n")
            web_entry.delete(0, END)
            # email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------UI SETUP --------------------------
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
web_entry.config(width=58)
web_entry.grid(row=1, column=1, columnspan=2, pady=5)
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
password_gen_button.config(text="Generate Password", font=FONT, height=1)
password_gen_button.grid(row=3, column=2, pady=5)

add_button = Button()
add_button.config(text="Add", font=FONT, height=1, width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
