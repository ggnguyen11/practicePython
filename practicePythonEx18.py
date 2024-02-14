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

# main function w/ counter, print statements and external function calls
# cannot have integer w/ leading 0, input = string
def main(count):
    guess = input("\nLet's play cows and bulls!\n" + "Can you guess the "\
                       + "4-digit number I am thinking of?\n")
    while True:
        count += 1
        print(answer)
        if guess == answer:
            print("You win!\n" + "You've guessed " + str(count) + " times.")
            return False
        elif len(guess) < 4:
            print("\nInvalid number.\n" + "Please guess a 4-digit number.\n"\
                  + "\nGuesses: " + str(count))
            return main(count)
        else:
# variable assignment for return values to be accessed via index
            cnb = get_cowsnbulls(guess)
            print("\nYou have " + str(cnb[0]) + " cows " + "and " + \
                  str(cnb[1]) + " bulls." + "\nGuesses: " + str(count))
            return main(count)

def get_cowsnbulls(guess):
    bulls = 0
    cows = 0
    i = 0
    guess_str = str(guess)
    while i < 4:
        if guess_str[i] == answer[i]:
            cows += 1
        elif guess_str[i] in answer:
            bulls += 1
        i += 1
# return statement for more than one value
    return cows, bulls

if __name__ == "__main__":
    main(count)