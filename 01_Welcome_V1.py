"""Version 1
This code will create a welcome screen for my quiz without using TKinter"""

print("Welcome to the Maori Quiz")

user_choice = input("Please enter an option:\n"
                    "1) Instructions\n"
                    "2) Start Quiz\n"
                    "3) Statistics\n"
                    "4) Exit\n")

if user_choice == "1":
    print("Instructions")

elif user_choice == "2":
    print("Start Quiz")

elif user_choice == "3":
    print("Statistics")

elif user_choice == "4":
    print("Goodbye")

