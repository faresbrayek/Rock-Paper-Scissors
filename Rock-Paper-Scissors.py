import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors!")
while True:
    user_choice = input(
        "Please enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice, please try again.")
        continue
    computer_choice = random.choice(choices)
    print(f"You chose {user_choice} and the computer chose {computer_choice}.")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Do you want to play again? (yes/no)").lower()
    if play_again == "no":
        print("Thanks for playing!")
        break
