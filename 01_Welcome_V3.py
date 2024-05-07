"""Version 3
This code is built off V2, now more aesthetically pleasing and will stop program when exit button is pressed """
import sys
from tkinter import *

root = Tk()

# Welcome Banner
root.title("WELCOME")
welcome = Label(root, bg="White", fg="Red", text="Welcome to the Māori Quiz",
                font=("Times", 20, "bold"))
options = Label(root, fg="Black", text="Please choose an option:",
                font=("Ariel", 10, "bold"))

welcome.pack(side=TOP)
options.pack(side=TOP)


# Instructions option
def instructions():
    print("Instructions")


# Start Quiz option
def start_quiz():
    print("Start Quiz")


# Sats option
def statistics():
    print("Statistics")


# Leave program option
def leave():
    print("Goodbye")
    sys.exit()


# Buttons for options
instructions_b1 = Button(root, text="Instructions", command=instructions).pack()
start_quiz_b2 = Button(root, text="Start Quiz", command=start_quiz).pack()
statistics_b3 = Button(root, text="Statistics", command=statistics).pack()
leave_b4 = Button(root, text="Exit", command=leave).pack()

root.mainloop()
