"""Version 1
Instructions are printed when asked for"""

# Get input
enter = input("Instructions? ").title()
if enter == "Yes":
    # Print instructions
    print("INSTRUCTIONS:\n"
          "When you press 'Start Quiz' you will be given two options for quiz type like this:\n"
          "<insert image>\n"
          "Once you choose a quiz type, there will be 10 questions on the subject of your choice, formatted as:\n"
          "<insert image>\n"
          "Choose the correct answer. When all the questions have been answered your final score will be shown.\n"
          "Enter you name then go to the 'Statistics' tab in the home screen to see your name on the leaderboard")
