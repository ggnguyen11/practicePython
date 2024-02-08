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
        print(answer)
        print("You have: " + str(num_cows(guess)) + " cows.")
        if guess == int(answer):
            print("You win!\n" + "You've guessed " + str(count) + " times.")
        elif len(str(guess)) < 4:
            print("\nInvalid number.\n" + "Please guess a 4-digit number.\n"\
                  + "\nGuesses: " + str(count))
            return main(count)

# function to return number of cows from given guess, initializing guessL list
# for appending -- str conversion for iteration and int conversion to append
def num_cows(guess):
    cows = 0
    guessL = []
    guess_str = str(guess)
    for char in guess_str:
        digit = int(char)
        guessL.append(digit)

    if guessL[0] == answer[0]:
        cows = 1
    elif guessL[0] == answer[0] and guessL[1] == answer[1]:
        cows = 2
    elif guessL[0] == answer[0] and guessL[1] == answer[1] and \
    guessL[2] == answer[2]:
        cows = 3
    elif guessL[0] == answer[0] and guessL[1] == answer[1] and \
    guessL[2] == answer[2] and guessL[3] == answer[3]:
        cows = 4

def num_bulls(guess):
    bulls = 0
    if guess[0] == answer[1] or guess[0] == answer[2] or guess[0] \
    == answer[3]:
        pass

if __name__ == "__main__":
    main(count)