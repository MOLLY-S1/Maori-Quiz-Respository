""" Version 5
Now using tkinter """

import random
from tkinter import *

root = Tk()


class Questions:
    def __init__(self, subject, question, answer, multi_choice_list):
        self.subject = subject
        self.question = question
        self.answer = answer
        self.multi_choice_list = multi_choice_list
        questions[subject][question] = answer


# Dictionary of questions and answers (as per the class)
questions = {"Colours": {}, "Numbers": {}}

# Questions to be entered
Questions("Numbers", 'Tahi', 'One', "num_list")
Questions("Numbers", 'Rua', 'Two', "num_list")
Questions("Numbers", "Toru", 'Three', "num_list")
Questions("Numbers", 'Whā', "Four", "num_list")
Questions("Numbers", 'Rima', "Five", "num_list")
Questions("Numbers", "Ono", "Six", "num_list")
Questions("Numbers", 'Whitu', "Seven", "num_list")
Questions("Numbers", 'Waru', "Eight", "num_list")
Questions("Numbers", 'Iwa', "Nine", "num_list")
Questions("Numbers", "Tekau", "Ten", "num_list")

Questions("Colours", 'Mā', 'White', "colour_list")
Questions("Colours", 'Whero', 'Red', "colour_list")
Questions("Colours", "Karaka", 'Orange', "colour_list")
Questions("Colours", 'Kōwhai', "Yellow", "colour_list")
Questions("Colours", 'Kākāriki', "Green", "colour_list")
Questions("Colours", "Mangu", "Black", "colour_list")
Questions("Colours", 'Kikorangi', "Blue", "colour_list")
Questions("Colours", 'Waiporoporo', "Purple", "colour_list")
Questions("Colours", 'Parauri', "Brown", "colour_list")
Questions("Colours", "Kiwikiwi", "Grey", "colour_list")

# List of numbers
num_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
colour_list = ["White", "Red", "Orange", "Yellow", "Green", "Black",
               "Blue", "Purple", "Brown", "Grey"]

# Quiz selection
pick = Label(root, text="Please choose a quiz to play: ")
pick.pack(side=TOP)

# Buttons
enter = ""


def colour():
    global enter
    enter = "Colour"


def number():
    global enter
    enter = "Number"


b1_colour = Button(root, text="Colours", command=colour)
b2_number = Button(root, text="Numbers", command=number)
b1_colour.pack(side=LEFT)
b2_number.pack(side=RIGHT)
mainloop()
print(enter)

d1 = list(questions[enter].items())
random.shuffle(d1)
questions[enter] = dict(d1)

# Get random question
for key in questions[enter]:
    question = key

    if enter == "Numbers":
        qlist = num_list
    else:
        qlist = colour_list

    # get two random numbers
    n1 = random.choice(qlist)

    # Ensure n1 != the answer
    while n1 == questions[enter][question]:
        n1 = random.choice(qlist)

    n2 = random.choice(qlist)

    # Ensure n2 != the answer or n1
    while n2 == questions[enter][question] or n2 == n1:
        n2 = random.choice(qlist)

    # List to add possible answers to
    answers = [n1, n2, questions[enter][question]]

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

    Label(root, text=f"What is the English word for {question}?").pack(side=TOP)
    b1 = Button(root, text={a1}).pack(side=LEFT)

