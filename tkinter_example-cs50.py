# tkinter resource:
# http://effbot.org/tkinterbook/

import random
import tkinter as tk

# Initialize window
window = tk.Tk()
# title
window.title("anime2kodi")
# geometry
window.geometry("400x350")


# Function(d)
def phrase_generator():
    phrases = ["Hello ", "Hi ", "Aloha "]
    name = str(ent01.get())
    return phrases[random.randint(0, 2)] + name


def phrase_display():
    greeting = phrase_generator()
    greeting_display = tk.Text(master=window, height=10, width=30)
    greeting_display.grid(column=0, row=3)
    greeting_display.insert(tk.END, greeting)


# Label(s)
lab01 = tk.Label(text="Welcome to my application!", font=("Times New Roman", 15))
lab01.grid(column=0, row=0)

lab02 = tk.Label(text="What is your name? ")
lab02.grid(column=0, row=1)

# Entry Field(s)
ent01 = tk.Entry()
ent01.grid(column=1, row=1)

# Button(s)
but01 = tk.Button(text="Click Me!", bg="grey", command=phrase_display)
but01.grid(column=0, row=2)

window.mainloop()
