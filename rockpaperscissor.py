

#stimulate computer choice
import random


# take input from user
user_action = input("Enter your choice (rock, paper, scissors):")

possible_actions = ["rock","scissor","paper"]

computer_action = random.choice(possible_actions)

print(f"\n You chose {user_action}, computer chose {computer_action}.\n")

# if same choices then results will be same
if user_action == computer_action:
  print(f"Both players selected {user_action}. Its a tie")


#user and computer making a choice
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")





