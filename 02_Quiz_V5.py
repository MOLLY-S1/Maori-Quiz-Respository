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

enter = ""
score = 0


# Main quiz function
def play():
    global score
    global asked_questions
    if len(asked_questions[enter]) == len(questions[enter]):
        print(f"Your score is {score}/10")
        return

    # Destroy previous question window if it exists
    if hasattr(play, "question_window") and play.question_window:
        play.question_window.destroy()

    new_window = Toplevel(root)

    # Ensure each question is only asked once
    question = random.choice([key for key in questions[enter] if key not in asked_questions[enter]])
    asked_questions[enter].append(question)

    new_window.title(f"What is the English word for {question}?")

    # Select correct list for random questions
    if enter == "Numbers":
        qlist = num_list
    else:
        qlist = colour_list

    # Ensure each question is unique
    n1 = random.choice(qlist)
    while n1 == questions[enter][question]:
        n1 = random.choice(qlist)

    n2 = random.choice(qlist)
    while n2 == questions[enter][question] or n2 == n1:
        n2 = random.choice(qlist)

    answers = [n1, n2, questions[enter][question]]
    random.shuffle(answers)

    # Buttons function
    def buttons(clicked_answer):
        answer_window = Toplevel(root)
        if clicked_answer == questions[enter][question]:
            Label(answer_window, text="CORRECT", fg="green").pack(side=TOP)
            global score
            score += 1
        else:
            Label(answer_window, text=f"INCORRECT\n The answer was {questions[enter][question]}", fg="red").pack(
                side=TOP)
        Button(answer_window, text="Next Question", command=lambda: [answer_window.destroy(), play()]).pack(side=BOTTOM)

    # Question Screen
    Label(new_window, text=f"What is the English word for {question}?").pack(side=TOP)
    # Make a button for each possible answer
    for answer in answers:
        Button(new_window, text=f"{answer}", command=lambda answer=answer: buttons(answer)).pack(side=TOP)

    play.question_window = new_window


def colour():
    global enter
    enter = "Colours"
    add_window.destroy()
    play()


def number():
    global enter
    enter = "Numbers"
    add_window.destroy()
    play()


# Quiz selection
add_window = Toplevel(root)
add_window.title("QUIZ OPTIONS")
pick = Label(add_window, text="Please choose a quiz to play: ")
pick.pack(side=TOP)

b1_colour = Button(add_window, text="Colours", command=colour)
b2_number = Button(add_window, text="Numbers", command=number)
b1_colour.pack(side=LEFT)
b2_number.pack(side=RIGHT)

asked_questions = {"Colours": [], "Numbers": []}  # Track asked questions

print(f"Your score is {score}/10")
root.mainloop()
