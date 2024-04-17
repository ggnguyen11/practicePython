# practicepython.org | exercise 25 | 04/17/2024
# guessing game two: you, as the user, will specify a number for the computer
# to guess. the program will try to guess the number and you will specify
# whether the number is too high, too low, or correct & print out the amount
# of guesses

import random

answer = int(input("Think of any number between 0 to 100 and I'll try to " + \
    "guess it: "))

guess = random.randint(0, 100)
count = 0

confirm = input("\nIs your number " + str(guess) + "?\n" + "Please enter " + \
    "\'y\' or \'n\'\n")

while confirm.lower() == 'n':
    deviation = input("Is your number higher or lower?\nPlease enter " + \
        "\'h\' or \'l\'\n")
    confirm = input("\nIs your number " + str(guess) + "?\n" + \
        "Please enter \'y\' or \'n\'\n")
    if confirm.lower() == 'y':
        print("Told you I could guess it.\nGuesses: " + str(count))