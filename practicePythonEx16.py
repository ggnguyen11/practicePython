# practicepython.org | exercise 16 | 01/29/2024
# prompt: write a password generator, mix of lowercase, uppercase, numbers
# and symbols -- newly generated random password each run
# include run-time code in a main method
# extra: ask user how strong they want their password to be
# for weak passwords, pick a word or two from a list

import random
import string

# initializing lists based on common fruits/colors
fruit = ['apple', 'banana', 'cherry', 'grapes', 'mango', 'orange']
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']

# main method function that prompts user for choice of password strength
def main():
    strength = input("Welcome to the password generator!\n\nHow strong do "\
                     + "you want your password to be?\n" + "Please select "\
                     + "'weak', 'average', or 'strong'.\n")
    if strength.lower() == "weak":
        print("\nYour new password is: " + weak_pass())
    elif strength.lower() == "average":
        print("\nYour new password is: " + str(avg_pass()))
    elif strength.lower() == "strong":
        print("\nYour new password is: " + str(strong_pass()))
    else:
        print("\nInvalid option. Please select 'weak', 'average' or 'strong'"\
              + "\n")
        return main()

# function to generate weak passwords, based on combination of common words
def weak_pass():
    wpass = random.choice(list(set(fruit).union(color)))
    if len(wpass) < 8:
        wpass += random.choice(list(set(color).union(fruit)))
    return wpass

# function to generate average passwords, length based on 2021 statistic:
# (64% of US respondents have passwords b/n 8-11 characters)
def avg_pass():
    apass = []
    for i in range(random.randint(8, 12)):
# compounds on weak_pass() by appending numbers
        apass = random.choice(list(set(fruit).union(color)))
        while len(apass) < 8:
            apass += str(random.randint(0, 9))
    return apass

def strong_pass():
    spass = []
# list of special characters allowed for use in passwords
    spchar = string.punctuation
    for i in range(random.randint(12, 18)):
# function to generate random strings composed of both lower/uppercase,
# numbers, and special characters
        spass += random.choice(string.ascii_letters)
        spass += str(random.randint(0, 9))
        spass += random.choice(spchar)
    return spass

# function to generate strong passwords
# code block that checks for main function to be run at script execution
if __name__ == "__main__":
    main()