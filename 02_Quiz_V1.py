""" Version 1
Generates random question from dictionary"""

import random

# List of questions
questions = {'Tahi': 'one', 'Rua': 'two', "Toru": 'three', 'Whā': "four", 'Rima': "five",
             "Ono": "six", 'Whitu': "seven", 'Waru': "eight", 'Iwa': "nine", "Tekau": "ten"}

# Get random question
question = random.choice(list(questions.keys()))

print(f"What is the English word for {question}?")