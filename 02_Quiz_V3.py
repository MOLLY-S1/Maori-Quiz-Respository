""" Version 3
Questions now stored in class 'Questions' and are randomly chosen through the whole list"""

import random


class Questions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        questions[question] = answer


# Dictionary of questions and answers (as per the class)
questions = {}

Questions('Tahi', 'One')
Questions('Rua', 'Two')
Questions("Toru", 'Three')
Questions('Whā', "Four")
Questions('Rima', "Five")
Questions("Ono", "Six")
Questions('Whitu', "Seven")
Questions('Waru', "Eight")
Questions('Iwa', "Nine")
Questions("Tekau", "Ten")

# List of numbers
num_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]


# Get random question
for i in questions:
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
