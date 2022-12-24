import random

choices = ["rock", "paper", "scissors"]
cpu = random.choice(choices)
player = input("Rock, paper, or scissors? ").lower()

if player == cpu:
    print("Tie!")
    answer = input("Do you want to play again? y/n: ").lower()
    while answer == "y":
        cpu = random.choice(choices)
        player = input("Rock, paper, or scissors? ").lower()
        if player == cpu:
            print("Tie!")
        elif player == "rock":
            if cpu == "paper":
                print("You lose!")
            else:
                print("You win!")
        elif player == "paper":
            if cpu == "scissors":
                print("You lose!")
            else:
                print("You win!")
        elif player == "scissors":
            if cpu == "rock":
                print("You lose!")
            else:
                print("You win!")
        else:
            print("Invalid input")
        answer = input("Do you want to play again? y/n: ").lower()
    else:
        print("Goodbye!")