#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: September 2019
# this function checks if the user guess the number


import random


def main():
    # this function checks if the user guess the number 5

    # input
    print("Guess what number I'm thinking of! (between 1 & 100)")
    randomanswer = random.randint(1, 100)  # a number between 1 and 100
    guess = int(input("Enter your guess: "))

    # process
    if guess == randomanswer:
        # output
        print("")
        print("You are correct!")
    else:
        print("")
        print("Sorry, the number I was thinking of was", randomanswer, ".")


if __name__ == "__main__":
    main()
