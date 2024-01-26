# practicepython.org | exercise 1 | 01/19/2024
# prompt: write a program that asks the user for their name and age, then
# returns the year in which they turn 100 years old.
# gathering input and storing into variables for reuse
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

# storing current year in variable
currentYear = 2024

# calculation & print statement for year that user will turn 100 years old
# \ for line continuation
hundredthYear = (100 - age) + currentYear
print("Hello, " + name + "! " + "You will turn 100 years old in the year " +\
       str(hundredthYear) + ".")

# extras
# 1. add onto the previous program by asking the user for another number and
# printing out that many copies of the previous message
# 2. print out that many copies of the previous message on separate lines
repeat = int(input("Please gve me another number: "))
for i in range(repeat):
    if i < repeat:
        print("Hello, " + name + "! " + "You will turn 100 years old in the\
               year " + str(hundredthYear) + ".")