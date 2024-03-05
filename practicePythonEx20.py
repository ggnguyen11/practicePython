# practicepython.org | exercise 20 | 02/14/2024
# prompt: write function taking ordered list of numbers (elements from
# smallest to largest) and another number. function decides whether or
# not the given number is inside the list and returns & print a boolean
# extras: use binary search
import random
import math

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

# solution w/ binary search, w/ functions to determine halves of given list
# midpoint function
def midpoint(lst):
# math.floor() function to round down
    mid = int(math.floor((len(lst) - 1) / 2))
    return mid

# variable for given number to be checked via binary search
binary_num = int(input("I will randomly generate an ordered list of numbers." \
    + "\nPlease provide a number to be checked if it is in the list.\n"))

# function implementing binary search, using median as a conditional
def num_inlist_binary(lst):
# print statement to display list for each iteration
    print(lst)
    mid = midpoint(lst)
    median = lst[mid]
# print statements for debugging
    #print("median: " + str(median))
    #print("mid: " + str(mid))
# conditionals to test for match case when the list has only two elements
    if mid == 1 and median == lst[1] and binary_num == median:
        print(str(binary_num) + " is within the generated list:\n" + \
              str(ordered_randlist))
        return True
    elif mid == 1 and binary_num != median:
        print(str(binary_num) + " is not within the generated list:\n" + \
                str(ordered_randlist))
        return False
# conditionals for when the list has more than two elements
    while mid > 1:
        if binary_num == median:
            #print("mid: " + str(mid))
            print(str(binary_num) + " is within the generated list:\n" + \
                str(ordered_randlist))
            return True
        elif mid == 0 and len(lst) == 1:
            #print("mid: " + str(mid))
            print(str(binary_num) + " is not within the generated list:\n" + \
                str(ordered_randlist))
            return False
# reminder that if/elif statements evaluate in pairs
        if binary_num < median:
# first half of the list up until the midpoint
            newlist = lst[0:mid]
            return num_inlist_binary(newlist)
        elif binary_num > median:
# other half of the list, starting at the midpoint until the endpoint
            newlist = lst[mid:len(lst)]
            return num_inlist_binary(newlist)

print(num_inlist_binary(ordered_randlist))