# practicepython.org | exercise 10 | 01/29/2024
# prompt: for lists a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], write program that returns
# only the elements that are common b/n lists w/o dupes; make sure program
# works on lists of two different sizes, write using at least one list comp.
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

def longer_list(l1, l2):
    if l1 > l2:
        return l1
    elif l2 > l1:
        return l2
    else:
        return l1

def shorter_list(l1, l2):
    if l1 < l2:
        return l1
    elif l2 < l1:
        return l2
    else:
        return l2

# list comprehension w/ conditional
c = [num for num in longer_list(a, b) if num in shorter_list(a, b) \
     and num not in c]

print(c)
# extra 1: randomly generate two lists to test
d = []
e = []
f = []

def randlist(l):
    for i in range(random.randint(1, 20)):
        l.append(random.randint(1, 100))
        i += 1
    return l

list_d = (randlist(d))
list_e = (randlist(e))

f = [num for num in longer_list(list_d, list_e) if num \
     in shorter_list(list_d, list_e) and num not in f]

print(f)