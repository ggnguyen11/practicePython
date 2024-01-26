# practicepython.org | exercise 2 | 01/19/2024
# prompt: ask the user for a number. return msg whether number is odd/even
number = int(input("Please give me a number: "))
# extra #1. if number is multiple of 4, print out different message
if number % 2 == 0 and number % 4 != 0:
    print("Your number is even!")
elif number % 2 != 0:
    print("Your number is odd!")
elif number % 4 == 0:
    print("Your number is both even and divisible by 4!")
# 2. ask user for 2 numbers: one number to check (num) and one number to
# divide by (check). if check divides evenly into num, inform the user.
# otherwise, print a different appropriate msg
num = int(input("Now, please give me another number to check: "))
check = int(input("Now, please give me a number to divide that by: "))
if num % check == 0:
    print(str(num) + " is evenly divisible by " + str(check) + "!")
elif num % check != 0:
    print(str(num) + " is not evenly divisble by " + str(check) + "!")