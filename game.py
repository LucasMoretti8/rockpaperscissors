import random

def __init__(self):
    print("Which one do you wanna be?")
    print("ROCK, PAPER, or SCISSORS")
    player = input("Your play: ").upper()

    while player not in {"ROCK", "PAPER", "SCISSORS"}:
        print("Invalid input. Please enter rock paper or scissors:")
        player = input("Your play: ").upper()

    list = ["ROCK", "PAPER", "SCISSORS"]
    computer = random.choice(list)
    print("Player: " + player)
    print("Computer: " + computer)

    if (player == computer):
        print("TIE!!")

        
if(__name__ == "__main__"):
    start_game()