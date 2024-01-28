# practicepython.org | exercise 9 | 01/27/2024
# prompt: generate random number between 1 and 9, ask user to guess the number
# then say whether they guessed too low, high or exactly right
# import random module for use of random.randint()
import random
import sys

# initializing count & goal number
count = 0
num = str(random.randint(1, 9))

# loop function to determine if guess was correct
def right_num(num, guess):
    if guess == num:
        print("That's right!")
        return True
    elif guess > num and guess != "exit":
        print("Too high! Try again.")
        return False
    elif guess < num and guess != "exit":
        print("Too low! Try again.")
        return False

# function call
while True:
# extra 2: keep track of number of guesses, print that number when game ends
    count += 1
    guess = input("I'm thinking of a number between 1 and 9. Can you " \
                  + "guess it?\nType your guess here: ")
    if right_num(num, guess):
        sys.exit("Good job! " + str(count) + " guesses have been made.")
# extra 1: keep game going until the user types "exit"
    elif guess == "exit":
        sys.exit("Exiting...")
    else:
        continue