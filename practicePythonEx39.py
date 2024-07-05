# practicepython.org | exercise 39 | 07/05/2024
# create program that asks the user to enter their name & age, outputting how
# long it will be until they turn 100 years old; use datetime library

import datetime
# import time

# generates date object to be manipulated for date components
now = datetime.datetime.now()

def hundredth_year():
    name = input("Please enter your name:\n")
    birth_yr = int(input(f"\nHi {name}, in what year were you born?\n"))
    hundredth_yr = birth_yr + 100
    gap = hundredth_yr - now.year
    print(f"\nYou'll turn 100 years old in {gap} years.\n")
    
hundredth_year()