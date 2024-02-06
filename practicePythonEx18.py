# practicepython.org | exercise 18 | 02/06/2024
# prompt: create program that will play the "cows and bulls" game w/ the user
# rules: randomly generate a 4-digit number and ask the user to guess it
# for every digit that the user guessed correctly in the correct place, = cow
# every digit that is guessed correctly in the wrong place = bull
# every guess, print how many cows and bulls they have; keep track of guesses

import random

count = 0
def main():
    numstr = ''
    guess = int(input("Let's play cows and bulls!\n" + "Can you guess the " +\
                      "4-digit number I an thinking of?\n"))
    for i in range(4):
        numstr += str(random.randint(0, 9))
    print(numstr)
if __name__ == "__main__":
    main()