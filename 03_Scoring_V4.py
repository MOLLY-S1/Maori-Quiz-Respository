""" Version 4
Now using Tkinter"""

import random
from tkinter import *

root = Tk()

# Dictionary to store scores
scoreboard = {}


# Class to store scores from file
class Score:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        scoreboard[name] = f"{score}/10"


# Read off file
def generate_scoreboard():
    import csv
    with open('Scoreboard1.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            Score(line[0], line[1])


# MAIN ROUTINE
# Get name and score
get_score = random.randint(1, 10)
get_name = input("Enter Name:")

# Write on existing file
file = open('Scoreboard1.csv', 'a')
file.write(f"{get_name}, {get_score}\n")
file.close()
generate_scoreboard()

new_window = Toplevel(root)

# Sorting scoreboard
sorted_scores = sorted(scoreboard.items(), key=lambda x: int(x[1].split('/')[0]), reverse=True)
scoreboard = dict(sorted_scores)

Label(new_window, text="SCOREBOARD", fg="Black", font=("Times", 20, "bold")).pack()
for key, value in sorted_scores:
    Label(new_window, text=f"{key}: {value}").pack(side=TOP)
root.mainloop()

