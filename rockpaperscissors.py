import random
import time

class RockPaperScissors:

#Looping
    play = "y"
    while play != "n":

        print("Which one do you wanna be?")
        print("ROCK, PAPER, or SCISSORS")
        player = input("Your play: ").upper()

        while player not in {"ROCK", "PAPER", "SCISSORS"}:
            print("Invalid input. Please enter rock paper or scissors:")
            player = input("\n" + "Your play: ").upper()

        
        time.sleep(2)
        print("\n" + "READY!" + "\n")
        time.sleep(2)
        print("STEADY!" + "\n")
        time.sleep(2)
        print("GO!" + "\n")
        time.sleep(1)

        print("===================")

        list = ["ROCK", "PAPER", "SCISSORS"]
        computer = random.choice(list)
        print("Player: " + player)
        print("Computer: " + computer)

        print("===================")


        if (player == computer):
            print("      TIE!!")
        
        elif (player == "ROCK" and computer == "SCISSORS" or player == "SCISSORS" and computer == "PAPER" or player == "PAPER" and computer == "ROCK"):
             print("      YOU WIN!!")
        else:
             print("      YOU LOSE!!")

        print("===================" + "\n")


    
#Endgame
        print("Do you wanna play again?" + "\n" + "y for yes n for no:")
        play = input("Choose: ").upper()

#Validation
        while play not in {"Y", "N"}:
            print("Invalid input. Please enter 'y' or 'n':")
            play = input("Choose: ")

        if (play == "Y"):
                print("Ok, lets go again!")
                continue
        else:
            print("Ok! See ya!!")
            break
   