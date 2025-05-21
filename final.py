import random

item_list = ["rock", "paper", "scissors"]

user_choice = input("Enter your move (rock, paper, scissors): ").lower()
comp_choice = random.choice(item_list)

if user_choice not in item_list:
    print("Invalid input. Please enter rock, paper, or scissors.")
else:
    print(f"User choice: {user_choice}, Computer choice: {comp_choice}")

    if user_choice == comp_choice:
        print("Both chose the same: Match tie")

    elif user_choice == "rock":
        if comp_choice == "paper":
            print("Paper covers rock: Computer wins")
        else:
            print("Rock smashes scissors: You win")

    elif user_choice == "paper":
        if comp_choice == "scissors":
            print("Scissors cut paper: Computer wins")
        else:
            print("Paper covers rock: You win")

    elif user_choice == "scissors":
        if comp_choice == "rock":
            print("Rock smashes scissors: Computer wins")
        else:
            print("Scissors cut paper: You win")
