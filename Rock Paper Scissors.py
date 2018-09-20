'''
Title: Rock, Paper, Scissors
Author: Haamid Mohammed
Date Created: 18/09/19
'''
import random

def intro():
    print("Welcome to Rock, Paper, Scissors")
    
# Variables
score = 0
repeat = True
choice = 0
again = ""

# Code Starts Here
# Input
intro()
while again == "y" or again == "Y" or again == "":
    again = 1
    while not (choice == "1" or choice == "2" or choice == "3"):
        choice = input("Pick Rock(1), Paper(2), or Scissors(3): ")

    # Processing
    choice = int(choice)
    cc = random.randrange(3) # 0 is rock, 1 is paper, and 2 is scissors

    if choice == 1 and cc == 0 or choice == 2 and cc == 1 or choice == 3 and cc == 2:
        result = 1 # tie
    elif choice == cc or choice == 3 and cc == 0:
        result = 0 # lose
    else:
        result = 2 # win
        
    # output
    if choice == 1:
        print("You Chose Rock")
    elif choice == 2:
        print("You Chose Paper")
    elif choice == 3:
        print("You Chose Scissors")
    if cc == 0:
        print("The Computer Chose Rock")
    elif cc == 1:
        print("The Computer Chose Paper")
    elif cc == 2:
        print("The Computer Chose Scissors")
        
    if result == 0:
        print("You Lose.")
    elif result == 1:
        print("You Tied")
    elif result == 2:
        print("You Won")
    while not (again == "y" or again == "Y" or again == "" or again == "n" or again == "N"):
        again = input("Play again? (Y/N): ")
        
        
