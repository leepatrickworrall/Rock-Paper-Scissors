import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:

    user_input = input("Minigame - Rock, Paper, Scissors"
                       "\n- Rock"
                       "\n- Paper"
                       "\n- Scissors\n"
                       "\nPlease type one of the following. "
                       "Alternatively, you can type 'quit' to exit: ").lower()

    if user_input == "quit":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_num = random.randint(0, 2)
    # Rock: 0, Paper: 1, Scissors: 2
    computer_pick = options[random_num]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("You and the computer both chose the same option. Try again!")

    else:
        print("You lost.")
        computer_wins += 1

print("\nYou won", user_wins, "times.")
print("\nThe computer won", computer_wins, "times.")
print("\nGoodbye!")