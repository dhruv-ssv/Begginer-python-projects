import random

choices = ["rock", "paper", "scissors"]
cpu = random.choice(choices)
player = input("Rock, paper, or scissors? ").lower()

if player == cpu:
    print("Tie!")
    answer = input("Do you want to play again? y/n: ").lower()
    if answer == "y":
        player = input("Rock, paper, or scissors? ").lower()
    else:
        print("Thanks for playing!")
elif player == "rock":
    if cpu == "scissors":
        print("You win!")
        answer = input("Do you want to play again? y/n: ").lower()
        if answer == "y":
            player = input("Rock, paper, or scissors? ").lower()
        else:
            print("Thanks for playing!")
    else:
        print("You lose!")
        print(input("Do you want to play again? y/n: "))
        answer = input("Do you want to play again? y/n: ").lower()
        if answer == "y":
            player = input("Rock, paper, or scissors? ").lower()
        else:
            print("Thanks for playing!")
elif player == "paper":
    if cpu == "rock":
        print("You win!")
        answer = input("Do you want to play again? y/n: ").lower()
        if answer == "y":
            player = input("Rock, paper, or scissors? ").lower()
        else:
            print("Thanks for playing!")
    else:
        print("You lose!")
        answer = input("Do you want to play again? y/n: ").lower()
        if answer == "y":
            player = input("Rock, paper, or scissors? ").lower()
        else:
            print("Thanks for playing!")
elif player == "scissors":
    if cpu == "paper":
        print("You win!")
        answer = input("Do you want to play again? y/n: ").lower()
        if answer == "y":
            player = input("Rock, paper, or scissors? ").lower()
        else:
            print("Thanks for playing!")
    else:
        print("You lose!")
        answer = input("Do you want to play again? y/n: ").lower()
        if answer == "y":
            player = input("Rock, paper, or scissors? ").lower()
        else:
            print("Thanks for playing!")
else:
    print("Invalid input!")
    answer = input("Do you want to play again? y/n: ").lower()
    if answer == "y":
        player = input("Rock, paper, or scissors? ").lower()
    else:
        print("Thanks for playing!")
