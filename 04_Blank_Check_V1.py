"""Version 1, Blank Checker
This Component ensures all boxes are answered"""
from tkinter import *

root = Tk()



enter = ""


def check(entry, window):
    # Continue looping until valid is entered
    global enter
    # Remove surrounding whitespace
    enter = entry.get().strip()
    if enter == "":
        error_screen = Toplevel(root)
        new_window.destroy()
        Label(error_screen, text="That was not a valid input, please enter your name").pack(side=TOP)
        Button(error_screen, text="OK", command=error_screen.destroy).pack(side=TOP)
    else:
        window.destroy()
        print("Program Continues")



# Add top layer to root
new_window = Toplevel(root)

# User input
Label(new_window, text="Enter name below:").pack(side=TOP)
entry = Entry(new_window)
entry.pack(side=TOP)
enter = entry.get()
Button(new_window, text="ENTER", command=lambda: check(entry, new_window)).pack(side=TOP)



root.mainloop()
