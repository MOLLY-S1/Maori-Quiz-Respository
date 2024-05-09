""" Version 1
Trial 1, holds scores and names in a dictionary"""

import random

leaderboard = {}

score = random.randint(1, 10)
name = input("please enter name: ")

leaderboard[name] = score

print(leaderboard)


