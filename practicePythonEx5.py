# practicepython.org | exercise 5 | 01/26/2024
# prompt: take two lists, print their common elements (w/o dupes) and make
# sure that it works for two lists of different sizes
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c =

if a > b:
    longerlist = a
    otherlist = b
elif b > a:
    longerlist = b
    otherlist = a
for i in range(len(longerlist)):
    if longerlist[i] in otherlist:
        

# extra 1: randomly generate two lists to test

# extra 2: write this in one line of python