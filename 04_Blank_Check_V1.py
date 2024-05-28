"""Version 1, Blank Checker
This Component ensures all boxes are answered"""
from tkinter import *

root = Tk()

# Add top layer to root
new_window = Toplevel(root)


def check():
    # Continue looping until valid is entered
    global enter
    while enter == "":
        easygui.msgbox("Please answer all questions", "Error")
        enter = easygui.enterbox("Enter here:", "Enter")


# User input
Label(new_window, text="Enter name below:")
enter = Entry(new_window)
Button(new_window, text="ENTER", command=check)
