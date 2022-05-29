from tkinter import *
FONT = ("Calibri", 12, "bold")
# ---------------------PASSWORD GENERATOR ----------------


# ---------------------SAVE PASSWORD----------------------


# ---------------------UI SETUP --------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# ------------------------FORM------------------------------
web_name = Label()
web_name.config(text="Website", font=FONT)
web_name.grid(row=1, column=0)

web_entry = Entry()
web_entry.config(width=35)
web_entry.grid(row=1, column=0, columnspan=2)

password_gen = Button()
password_gen.config(text="Generate Password", font=FONT)
password_gen.grid(row=3, column= 2)







window.mainloop()
