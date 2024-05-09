""" Version 2
Generates random question from dictionary and 2 random + 1 correct answer and
produces them in a random order"""

import random

# Dictionary of questions and answers
questions = {'Tahi': 'One', 'Rua': 'Two', "Toru": 'Three', 'Whā': "Four", 'Rima': "Five",
             "Ono": "Six", 'Whitu': "Seven", 'Waru': "Eight", 'Iwa': "Nine", "Tekau": "Ten"}

# List of numbers
num_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

# Get random question
question = random.choice(list(questions.keys()))

# get two random numbers
n1 = random.choice(num_list)

# Ensure n1 != the answer
while n1 == questions[question]:
    n1 = random.choice(num_list)

n2 = random.choice(num_list)

# Ensure n2 != the answer or n1
while n2 == questions[question] or n2 == n1:
    n2 = random.choice(num_list)

# List to add possible answers to
answers = [n1, n2, questions[question]]

# Produce random answer order
a1 = random.choice(answers)

a2 = random.choice(answers)

# Ensure a2 != a1
while a2 == a1:
    a2 = random.choice(answers)

a3 = random.choice(answers)

# Ensure a3 != a1 or a2
while a3 == a1 or a3 == a2:
    a3 = random.choice(answers)

print(f"What is the English word for {question}?\n"
      f"Is it {a1}\n"
      f"Is it {a2}\n"
      f"Or is it {a3}")
