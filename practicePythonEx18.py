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
def main(count):
    guess = int(input("\nLet's play cows and bulls!\n" + "Can you guess the "\
                       + "4-digit number I am thinking of?\n"))
    while True:
        count += 1
        print(answer)
        if guess == int(answer):
            print("You win!\n" + "You've guessed " + str(count) + " times.")
            return False
        elif len(str(guess)) < 4:
            print("\nInvalid number.\n" + "Please guess a 4-digit number.\n"\
                  + "\nGuesses: " + str(count))
            return main(count)
        else:
            print("\nYou have " + str(num_cows(guess)) + " cows " + \
                  "and " + str(num_bulls(guess)) + " bulls.\n" + "Guesses: " \
                    + str(count))
            return main(count)

# function to return number of cows from given guess, initializing guess list,
# str conversion for iteration, infinite while loop w/ match case conditionals
def num_cows(guess):
    cows = 0
    guess_str = str(guess)
# conditional for single match instance for 1st, 2nd, 3rd or 4th place
    if (guess_str[0] == answer[0] and guess_str[1] != answer[1] and \
    guess_str[2] != answer[2] and guess_str[3] != answer[3]) or \
        (guess_str[1] == answer[1] and guess_str[0] != answer[0] and \
            guess_str[2] != answer[2] and guess_str[3] != answer[3]) or \
            (guess_str[2] == answer[2] and guess_str[0] != answer[0] and \
    guess_str[1] != answer[1] and guess_str[3] != answer[3]) or \
        (guess_str[3] == answer[3] and guess_str[0] != answer[0] and \
    guess_str[1] != answer[1] and guess_str[2] != answer[2]):
        cows = 1
# conditional for double match instance for 1st + 2nd, 1st + 3rd, 1st + 4th,
# 2nd + 3rd, 2nd + 4th, 3rd + 4th places
    elif (guess_str[0] == answer[0] and guess_str[1] == answer[1] and \
        guess_str[2] != answer[2] and guess_str[3] != answer[3]) or \
            (guess_str[0] == answer[0] and guess_str[2] == answer[2] and \
        guess_str[1] != answer[1] and guess_str[3] != answer[3]) or \
            (guess_str[0] == answer[0] and guess_str[3] == answer[3] and \
        guess_str[0] != answer[0] and guess_str[2] != answer[2]) or \
            (guess_str[1] == answer[1] and guess_str[2] == answer[2] and \
        guess_str[0] != answer[0] and guess_str[3] != answer[3]) or \
            (guess_str[1] == answer[1] and guess_str[3] == answer[3] and \
        guess_str[0] != answer[0] and guess_str[2] != answer[2]) or \
            (guess_str[2] == answer[2] and guess_str[3] == answer[3] and \
        guess_str[0] != answer[0] and guess_str[1] != answer[1]):
        cows = 2
# conditional for triple match instance for 1st + 2nd + 3rd, 1st + 2nd + 4th,
# 1st + 3rd + 4th, 2nd + 3rd + 4th
    elif (guess_str[0] == answer[0] and guess_str[1] == answer[1] and \
        guess_str[2] == answer[2] and guess_str[3] != answer[3]) or \
            (guess_str[0] == answer[0] and guess_str[1] == answer[1] and \
        guess_str[3] == answer[3] and guess_str[2] != answer[2]) or \
            (guess_str[0] == answer[0] and guess_str[2] == answer[2] and \
        guess_str[3] == answer[3] and guess_str[1] != answer[1]) or \
            (guess_str[1] == answer[1] and guess_str[2] == answer[2] and \
        guess_str[3] == answer[3] and guess_str[0] != answer[0]):
        cows = 3
    elif guess_str[0] == answer[0] and guess_str[1] == answer[1] and \
        guess_str[2] == answer[2] and guess_str[3] == answer[3]:
        cows = 4
    return cows

def num_bulls(guess):
    bulls = 0
    guess_str = str(guess)
# checking for element within string, but not match case for exact position
    while guess_str[0] != answer[0] and guess_str[1] != answer[1] and \
    guess_str[2] != answer[2] and guess_str[3] != answer[3]:
# checking for single instance in answer
        if (guess_str[0] in set(answer)) or (guess_str[1] in set(answer)) or \
            (guess_str[2] in set(answer)) or (guess_str[3] in set(answer)):
            bulls = 1
# checking for two instances in answer: 1st + 2nd, 1st + 3rd, 1st + 4th,
# 2nd + 3rd, 2nd + 4th, 3rd + 4th
        elif (guess_str[0] in set(answer)) and (guess_str[1] in set(answer)) \
        or (guess_str[0] in set(answer)) and (guess_str[2] in set(answer)) \
        or (guess_str[0] in set(answer)) and (guess_str[3] in set(answer)) \
        or (guess_str[1] in set(answer)) and (guess_str[2] in set(answer)) \
        or (guess_str[1] in set(answer)) and (guess_str[3] in set(answer)) \
        or (guess_str[2] in set(answer)) and (guess_str[3] in set(answer)):
            bulls = 2
# checking for three instances in answer: 1st + 2nd + 3rd, 1st + 2nd + 4th,
# 1st + 3rd + 4th, 2nd + 3rd + 4th
        elif (guess_str[0] in set(answer) and guess_str[1] in set(answer) \
        and guess_str[2] in set(answer)) or \
        (guess_str[0] in set(answer) and guess_str[1] in set(answer) \
        and guess_str[3] in set(answer)) or \
        (guess_str[0] in set(answer) and guess_str[2] in set(answer) \
        and guess_str[3] in set(answer)) or \
        (guess_str[1] in set(answer) and guess_str[2] in set(answer) \
        and guess_str[3] in set(answer)):
            bulls = 3
        elif (guess_str[0] in set(answer) and guess_str[1] in set(answer) \
        and guess_str[2] in set(answer) and guess_str[3] in set(answer)):
            bulls = 4
    return bulls

if __name__ == "__main__":
    main(count)