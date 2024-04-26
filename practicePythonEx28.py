# practicepython.org | exercise 28 | 04/26/2024
# implement function that takes 3 variables as input & returns the largest
# number, w/o using the max() function

numOne = int(input("Give me three numbers and I'll tell you which one is " + \
    "the largest.\n1st number:\n"))
numTwo = int(input("\n2nd number:\n"))
numThree = int(input("\n3rd number:\n"))

def largest(one, two, three):
    if one > two and one > three:
        print(str(one) + " is the largest of the three.")
    elif two > one and two > three:
        print(str(two) + " is the largest of the three.")
    elif three > one and three > two:
        print(str(three) + " is the largest of the three.")

largest(numOne, numTwo, numThree)