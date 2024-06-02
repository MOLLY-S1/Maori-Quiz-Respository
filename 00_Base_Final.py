"""FINAL CODE
Base component made of all other components"""

import sys
from tkinter import *
import random

root = Tk()


# Class for questions, including questions, answer and subject
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

# List of numbers and colours for multi-choice
num_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
colour_list = ["White", "Red", "Orange", "Yellow", "Green", "Black",
               "Blue", "Purple", "Brown", "Grey"]

# Defining global variable enter
enter = ""


# Blank Checking function
def check(entry, window):
    # Continue looping until valid is entered
    global enter
    # Remove surrounding whitespace
    enter = entry.get().strip()
    if enter == "":
        error_screen = Toplevel(root)
        error_screen.title = "ERROR"
        Label(error_screen, text="That was not a valid input, please enter your name").pack(side=TOP)
        Button(error_screen, text="OK", command=error_screen.destroy).pack(side=TOP)
    else:
        window.destroy()
        # Add score and name to file
        with open('Scoreboard1.csv~', 'a') as file:
            file.write(f"{enter}, {score}\n")
        return


# Defining global variables score and name
score = 0
name = ""


# Start Quiz option
def quiz():
    enter = ""
    global score
    score = 0
    asked_questions = []

    # Main quiz function
    def play():
        global score
        nonlocal asked_questions

        # Exiting at end of quiz
        if len(asked_questions[enter]) == len(questions[enter]):
            play.question_window.destroy()

            # Show player score
            new_window = Toplevel(root)
            Label(new_window, text=f"Your score is {score}/10", fg="Black").pack()
            Label(new_window, text="Name: ").pack()

            # Get name
            name_entry = Entry(new_window)
            name_entry.pack()

            Button(new_window, text="Exit", command=lambda: check(name_entry, new_window)).pack()
            return

        # Destroy previous question window
        if hasattr(play, "question_window") and play.question_window:
            play.question_window.destroy()

        new_window = Toplevel(root)
        new_window.title("QUIZ")

        # Ensure each question is only asked once
        question = random.choice([key for key in questions[enter] if key not in asked_questions[enter]])
        asked_questions[enter].append(question)

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
            answer_window.title("ANSWER")
            if clicked_answer == questions[enter][question]:
                Label(answer_window, text="CORRECT", fg="green").pack(side=TOP)
                global score
                score += 1
            else:
                Label(answer_window, text=f"INCORRECT\n The answer was {questions[enter][question]}", fg="red").pack(
                    side=TOP)
            Button(answer_window, text="Next Question", command=lambda: [answer_window.destroy(), play()]).pack(
                side=BOTTOM)

        # Question Screen
        Label(new_window, text=f"What is the English word for {question}?").pack(side=TOP)
        # Make a button for each possible answer
        for answer in answers:
            Button(new_window, text=f"{answer}", command=lambda answer=answer: buttons(answer)).pack(side=TOP)

        play.question_window = new_window

    # For when colour option pressed
    def colour():
        nonlocal enter
        enter = "Colours"
        add_window.destroy()
        play()

    # For when number option pressed
    def number():
        nonlocal enter
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

    root.mainloop()


# Instructions Option
def instructions():
    instructions_window = Toplevel(root)
    instructions_window.title("INSTRUCTIONS")

    # Starting the quiz
    def start_quiz():
        instructions_window.destroy()
        quiz()

    Label(instructions_window, text="INSTRUCTIONS:\n"
                                    "When you press 'Start Quiz' you will be given two options for quiz "
                                    "type.\n"
                                    "Once you choose a quiz type, there will be 10 questions on the subject "
                                    "of your choice. "
                                    "Choose the correct answer. When all the questions have been "
                                    "answered your final score will be shown.\n"
                                    "Enter your name then go to the 'Statistics' tab "
                                    "in the home screen to see your name on the leaderboard!").pack(side=TOP)
    Button(instructions_window, text="Start Quiz", command=start_quiz).pack()
    Button(instructions_window, text="Return to Menu", command=lambda: instructions_window.destroy()).pack()
    root.mainloop()


# Statistics option
def statistics():
    # Dictionary to store scores
    scoreboard = {}

    # Scoring function
    def scoring():
        nonlocal scoreboard

        # Class to store scores from file
        class Score:
            def __init__(self, name, score):
                self.name = name
                self.score = score
                scoreboard[name] = f"{score}/10"

        # Read off file
        def generate_scoreboard():
            import csv
            with open('Scoreboard1.csv~', newline='') as csvfile:
                filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
                for line in filereader:
                    Score(line[0], line[1])

        # New window to show scoreboard
        new_window = Toplevel(root)
        new_window.title("SCOREBOARD")

        # Show current scores and add them to the board
        generate_scoreboard()

        # Sorting scoreboard
        sorted_scores = sorted(scoreboard.items(), key=lambda x: int(x[1].split('/')[0]), reverse=True)
        scoreboard = dict(sorted_scores)

        Label(new_window, text="SCOREBOARD", fg="Black", font=("Times", 20, "bold")).pack()
        place = 1
        for key, value in sorted_scores:
            Label(new_window, text=f"{place}. {key}: {value}").pack(side=TOP)
            place += 1
        Button(new_window, text="Exit", command=lambda: new_window.destroy()).pack(side=TOP)
        root.mainloop()

    scoring()


# Leave program option
def leave():
    print("Goodbye")
    sys.exit()


# Welcome Screen
def welcome_screen():
    # Welcome Banner
    root.title("WELCOME")
    welcome = Label(root, bg="White", fg="Red", text="Welcome to the Māori Quiz",
                    font=("Times", 20, "bold"))
    options = Label(root, fg="Black", text="Please choose an option:",
                    font=("Ariel", 10, "bold"))

    welcome.pack(side=TOP)
    options.pack(side=TOP)

    # Buttons for options
    Button(root, text="Instructions", command=instructions).pack()
    Button(root, text="Start Quiz", command=quiz).pack()
    Button(root, text="Statistics", command=statistics).pack()
    Button(root, text="Exit", command=leave).pack()

    root.mainloop()


# MAIN ROUTINE
welcome_screen()
root.mainloop()
