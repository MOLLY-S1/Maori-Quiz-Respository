""" Version 2
Trial 2, adds names to a file and reads off the file."""

# Dictionary to store scores
scoreboard = {}


# Class to store scores from file
class Score:
    def __init__(self, name, score):
        self.name = name
        print(name)
        self.score = score
        print(score)
        scoreboard[name] = f"{score}/10"




# Read off file
def generate_scoreboard():
    import csv
    with open('Scoreboard.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            Score(line[0], line[1])


print(scoreboard)
