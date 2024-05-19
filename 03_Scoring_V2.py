""" Version 2
Trial 2, adds names to a file and reads off the file."""

# Dictionary to store scores
scoreboard = {}


# Class to store scores
class Score:
    def __init__(self, name, score):
        self.name = name
        self.score = f"{score}/10"
        scoreboard[name] = score


# Read off file
def generate_scoreboard():
    import csv
    with open('Scoreboard.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            Score(line[0], line[1])


print(scoreboard)
