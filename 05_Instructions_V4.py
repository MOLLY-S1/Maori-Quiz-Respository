"""Version 4
Now a function"""

from tkinter import *

root = Tk()
instructions_window = Toplevel(root)


# Return home
def return_home():
    print("Return to home screen")


# Start Quiz
def start_quiz():
    print("Start Quiz")


# Instructions
def instructions():
    instructions_window = Toplevel(root)
    Label(instructions_window, text="INSTRUCTIONS:\n"
                                    "When you press 'Start Quiz' you will be given two options for quiz "
                                    "type.\n"
                                    "Once you choose a quiz type, there will be 10 questions on the subject "
                                    "of your choice. "
                                    "Choose the correct answer. When all the questions have been "
                                    "answered your final score will be shown.\n"
                                    "Enter you name then go to the 'Statistics' tab "
                                    "in the home screen to see your name on the leaderboard!").pack(side=TOP)
    Button(instructions_window, text="Start Quiz", command=quiz).pack()
    Button(instructions_window, text="Return to Menu", command=exit(instructions)).pack()




Button(root, text="Instructions", command=instructions).pack()

root.mainloop()
