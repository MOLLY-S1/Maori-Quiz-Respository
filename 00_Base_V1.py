"""Version 1
Base component to add all smaller components to, full code"""

import sys
from tkinter import *

root = Tk()


# Instructions option
def instructions():
    print("Instructions")


# Start Quiz option
def start_quiz():
    print("Start Quiz")


# Stats option
def statistics():
    print("Statistics")


# Leave program option
def leave():
    print("Goodbye")
    sys.exit()


def welcome_screen():
    # Welcome Banner
    root.title("WELCOME")
    welcome = Label(root, bg="White", fg="Red", text="Welcome to the Māori Quiz",
                    font=("Times", 20, "bold"))
    options = Label(root, fg="Black", text="Please choose an option:",
                    font=("Ariel", 10, "bold"))

    welcome.pack(side=TOP)
    options.pack(side=TOP)

    # Buttons for options
    Button(root, text="Instructions", command=instructions).pack()
    Button(root, text="Start Quiz", command=start_quiz).pack()
    Button(root, text="Statistics", command=statistics).pack()
    Button(root, text="Exit", command=leave).pack()

    root.mainloop()


welcome_screen()
