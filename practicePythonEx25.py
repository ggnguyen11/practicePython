# practicepython.org | exercise 25 | 04/17/2024
# guessing game two: you, as the user, will specify a number for the computer
# to guess. the program will try to guess the number and you will specify
# whether the number is too high, too low, or correct & print out the amount
# of guesses

import random

answer = int(input("Think of any number between 0 to 100 and I will " + \
    "guess it: "))

# initializing guess, count, lower and upper for while loop
guess = random.randint(0, 100)
count = 0
lower = 0
upper = 100

# initial guess
confirm = input("\nIs your number " + str(guess) + "?\n" + "Please enter " + \
    "\'y\' or \'n\'\n")
count += 1

while confirm.lower() == 'n':
    count += 1
    deviation = input("\nIs your number higher or lower?\nPlease enter " + \
        "\'h\' or \'l\'\n")
    if deviation == 'l':
        upper = guess
# -1 to upper bound to prevent redundancy
        guess = random.randint(lower, upper - 1)
    elif deviation == 'h':
        lower = guess
# + 1 to lower bound to prevent redundancy
        guess = random.randint(lower + 1, upper)
    confirm = input("\nIs your number " + str(guess) + "?\n" + \
        "Please enter \'y\' or \'n\'\n")

if confirm.lower() == 'y':
    print("\nTold you I could guess it.\nGuesses: " + str(count))
#    print(guesses)