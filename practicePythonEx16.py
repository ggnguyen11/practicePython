# practicepython.org | exercise 16 | 01/29/2024
# prompt: write a password generator, mix of lowercase, uppercase, numbers
# and symbols -- newly generated random password each run
# include run-time code in a main method
# extra: ask user how strong they want their password to be
# for weak passwords, pick a word or two from a list

import random
import string

# main method function that prompts user for choice of password strength
def main():
    strength = input("Welcome to the password generator!\n\nHow strong do "\
                     + "you want your password to be?\n" + "Please select "\
                     + "'weak', 'average', or 'strong'.\n")
    if strength.lower() == "weak":
        print("\nYour new password is: " + weak_pass())
    elif strength.lower() == "average":
        pass
    elif strength.lower() == "strong":
        pass
    else:
        print("\nInvalid option. Please select 'weak', 'average' or 'strong'"\
              + "\n")
        return main()

# function to generate weak passwords, based on common words
def weak_pass():
    fruit = ['apple', 'banana', 'cherry', 'grapes', 'mango', 'orange']
    color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
    return random.choice(list(set(fruit).union(color)))

# function to generate average passwords, length based on 2021 statistic:
# (64% of US respondents have passwords b/n 8-11 characters)
def avg_pass():
    alpha = []
    for i in range(random.randint(7, 16)):
# function to generate random strings composed of both lower/uppercase
        alpha.append(random.choice(string.ascii_letters))

# function to generate strong passwords
# code block that checks for main function to be run at script execution
if __name__ == "__main__":
    main()