from tkinter import *

FONT = ("Calibre", 12, "normal")
# ---------------------PASSWORD GENERATOR ----------------


# ---------------------SAVE PASSWORD----------------------


# ---------------------UI SETUP --------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=20)

canvas = Canvas(height=200, width=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1, pady=20)

# ------------------------FORM------------------------------
web_name = Label()
web_name.config(text="Website:", font=FONT)
web_name.grid(row=1, column=0)

web_entry = Entry()
web_entry.config(width=50)
web_entry.grid(row=1, column=1, columnspan=2)

email_name = Label()
email_name.config(text="Email/Username:", font=FONT)
email_name.grid(row=2, column=0)

email_entry = Entry()
email_entry.config(width=50)
email_entry.grid(row=2, column=1, columnspan=2)

password_gen = Button()
password_gen.config(text="Generate Password", font=FONT)
password_gen.grid(row=3, column=2)

window.mainloop()
