# practicepython.org | exercise 20 | 02/14/2024
# prompt: write function taking ordered list of numbers (elements from
# smallest to largest) and another number. function decides whether or
# not the given number is inside the list and returns & print a boolean
# extras: use binary search
import random

def gen_randlist():
    randlist = []
    for i in range(9):
        randlist.append(random.randint(1, 9))
# altering original randlist to be ordered
    randlist.sort()
    print(randlist)
    return randlist

# function call in global variable to be called within next function
ordered_randlist = gen_randlist()

def num_inlist():
    num = int(input("I will randomly generate an ordered list of numbers.\n" \
        + "Please provide a number to be checked if it is in the list.\n"))
    if num in ordered_randlist:
        return True
    else:
        return False

#print(num_inlist())

# solution w/ binary search, list_halver() function to determine middle of
# given list
def list_halver(Lst):
    halved_list = round(len(Lst) / 2)
    return int(halved_list)

# initializing global variable to be modified by function below
midpoint = list_halver(ordered_randlist)
list_half = []
# variable for given number to be checked via binary search
binary_num = int(input("I will randomly generate an ordered list of numbers." \
    + "\nPlease provide a number to be checked if it is in the list.\n"))

# function implementing binary search, using median as a conditional
def num_inlist_binary():
    global midpoint
    global list_half
    median = ordered_randlist[midpoint]
    if binary_num < median:
        print(median)
        #list_half = ordered_randlist[0:midpoint]
        #halved = list_halver(list_half)
        #midpoint = ordered_randlist[halved]
        #return num_inlist_binary()
    elif binary_num > median:
        print(median)
        #list_half = ordered_randlist[midpoint:-1]
        #halved = list_halver(list_half)
        #midpoint = ordered_randlist[halved]
        #return num_inlist_binary()
    elif binary_num == median:
        print(str(binary_num) + " is within the generated list:\n" + \
            str(ordered_randlist))
        return False
    else:
        print(str(binary_num) + " is not within the generated list:\n" + \
            str(ordered_randlist))
        return False

print(num_inlist_binary())