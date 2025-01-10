#Name
#Date
#Guessing Game

import random


def guessNumber(): #This Function gives you one try to guess a number from 1 - 10 and if you lose it shows you what that number was.
    print("Welcome to Random Number Guesser")
    print("In this game, you need to guess what the number is from 0-10.")
    guessingNumber = int(input("Enter Number"))
    Number = random.randint(0,10)
    if guessingNumber == Number:
         print("You win, congratulations and thank you for playing Random Number Guesser!")
    else:
        print("You lost" + " " + "The Number was" + " " + str(Number))

#Main

guessNumber()
