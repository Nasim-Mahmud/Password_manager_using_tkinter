from tkinter import *

# ---------------------PASSWORD GENERATOR ----------------


# ---------------------SAVE PASSWORD----------------------


# ---------------------UI SETUP --------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50)

canvas = Canvas()
lock_image = PhotoImage("logo.ong")
canvas.create_image(256, 256, image=lock_image)

window.mainloop()
