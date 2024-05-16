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


def play():
    count = 0

    d1 = list(questions[enter].items())
    random.shuffle(d1)
    questions[enter] = dict(d1)

    # Get random question
    for key in questions[enter]:
        new_window = Toplevel(root)

        count += 1
        new_window.title = f"Question {count}"
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

        def buttons(clicked_answer):
            new_window.destroy()
            answer_window = Toplevel(add_window)
            if clicked_answer == questions[enter][question]:
                Label(answer_window, text="CORRECT", fg="Green").pack(side=TOP)
                Button(answer_window, text="Next Question", command=answer_window.destroy).pack(side=BOTTOM)

            else:
                Label(answer_window, text="INCORRECT", fg="Red").pack(side=TOP)
                Button(answer_window, text="Next Question", command=answer_window.destroy).pack(side=BOTTOM)
                answer_window.mainloop()
            answer_window.mainloop()


        Label(new_window, text=f"What is the English word for {question}?").pack(side=TOP)
        Button(new_window, text=f"{a1}", command=lambda: buttons(a1)).pack(side=TOP)
        Button(new_window, text=f"{a2}", command=lambda: buttons(a2)).pack(side=TOP)
        Button(new_window, text=f"{a3}", command=lambda: buttons(a3)).pack(side=TOP)
        new_window.mainloop()




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
add_window.title = "QUIZ OPTIONS"
pick = Label(add_window, text="Please choose a quiz to play: ")
pick.pack(side=TOP)

b1_colour = Button(add_window, text="Colours", command=colour)
b2_number = Button(add_window, text="Numbers", command=number)
b1_colour.pack(side=LEFT)
b2_number.pack(side=RIGHT)

add_window.mainloop()
