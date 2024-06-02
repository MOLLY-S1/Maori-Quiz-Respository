""" Version 1
Trial 1, holds scores and names in a dictionary"""

import random

leaderboard = {"Molly": 5, "Jireh": 8, "Katelyn": 2}

# Get name and score
score = random.randint(1, 10)
name = input("please enter name: ")

leaderboard[name] = score

print(leaderboard)
