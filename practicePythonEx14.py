# practicepython.org | exercise 14 | 01/29/2024
# prompt: write a function that takes a list and returns a new list containing
# all elements of the first list minus all duplicates
# sample list w/ dupes to test
a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7]
b = []

# extra 1: write two different functions -- one using a loop and constructing
# a list, and another using sets
def no_dupes_set(list):
    return set(list)

print(no_dupes_set(a))

# sample solution w/ sets -- DONT use "list" as variable, as list() is a
# built-in function
def no_dupes_set_sample(l1):
    return list(set(l1))

print(no_dupes_set_sample(a))

def no_dupes_loop(list, newlist):
    for i in list:
        if i not in newlist:
            newlist.append(i)
        else:
            continue
        i += 1
    print(newlist)

no_dupes_loop(a, b)

# sample solution with list initialization within function
def no_dupes_sample(list):
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)
    return newlist

print(no_dupes_sample(a))
# extra 2: go back and solve exercise 5 using sets, write solution in function
# ex5: for two lists of different sizes, print out common elements w/o dupes
c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def no_dupes_ex5(list1, list2):
    print(set(list1).intersection(list2))

no_dupes_ex5(c, d)