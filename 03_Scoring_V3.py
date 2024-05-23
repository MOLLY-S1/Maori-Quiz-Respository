""" Version 3
Now gets new name and score and adds it to the file, then prints the scoreboard in order"""

import random

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
    with open('Scoreboard.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            Score(line[0], line[1])


# MAIN ROUTINE
# Get name and score
score = random.randint(1, 10)
name = input("Enter Name:")

# Write on existing file
file = open('Scoreboard.csv', 'a')
file.write(f"{name}, {score}\n")
file.close()
generate_scoreboard()

# Sorting scoreboard
sorted_scores = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)
scoreboard = dict(sorted_scores)
print(scoreboard)
