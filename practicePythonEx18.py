# practicepython.org | exercise 18 | 02/06/2024
# prompt: create program that will play the "cows and bulls" game w/ the user
# rules: randomly generate a 4-digit number and ask the user to guess it
# for every digit that the user guessed correctly in the correct place, = cow
# every digit that is guessed correctly in the wrong place = bull
# every guess, print how many cows and bulls they have; keep track of guesses

import random

# function to generate a 4-digit random number as a string
def gen_answer():
    numstr = ''
    for i in range(4):
        numstr += str(random.randint(0, 9))
    return numstr

# initializing count and assigning the random 4-digit number to a variable
# so as to be "immutable" for other functions
count = 0
answer = gen_answer()

def main(count):
    guess = int(input("Let's play cows and bulls!\n" + "Can you guess the " +\
                      "4-digit number I an thinking of?\n"))
    while guess != int(answer):
        count += 1
        if guess == int(answer):
            print("You win!\n" + "You've guessed " + str(count) + " times.")
            return main()
        elif len(str(guess)) < 4:
            print("\nInvalid number.\n" + "Please guess a 4-digit number.\n"\
                  + "\nGuesses: " + str(count))
            return main(count)

def cows(guess, numstr):
    num_cows = ''
    pass

def bulls():
    pass

if __name__ == "__main__":
    main(count)