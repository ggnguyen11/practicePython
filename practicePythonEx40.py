# practicepython.org | exercise 40 | 07/05/2024
# w/ a randomly generated number b/n 1 & 9, ask user for a guess and then say
# whether the guess is too low/too high/exactly right; if user does not guess
# b/n 1 and 9, tell them & don't count the guess

import random

# initializing count & goal number
count = 0
goal = random.randint(1, 9)
# print(f"Answer: {goal}\n")

# function to check guesses
def guesser(count):
    while True:
        while True:
# try/except block to catch ValueError & comparison operators to check for
# numbers outside bounds
            try:
                guess = int(input("\nI'm thinking of a number between 1 " + \
                    "and 9.\nWhat's your guess?\n"))
                if 1 <= guess <= 9:
                    break
                else:
                    print("\nInvalid input. Number must be from 1 to 9.\n")
            except ValueError:
                print("\nValueError, please enter a number from 1 to 9.\n")
        count += 1
        if guess == goal:
            break
    print(f"Congrats! It took you {count} guesses.\n")

guesser(count)