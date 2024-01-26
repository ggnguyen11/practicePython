# practicepython.org | exercise 3 | 01/25/2024
# prompt: for list a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], print elements
# less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)
    i += 1
# extra 1: instead of printing elements 1 by 1, make new list with all
# elements less than 5 and print new list
b = []
for i in a:
    if i < 5:
        b.append(i)
    i += 1
print(b)
# extra 2: write the solution in one line of code
print([i for i in a if i < 5])
# extra 3: ask user for number and return list containing only elements from
# original list a that are smaller than the given number
c = []
n = int(input("Please give me a number: "))
for i in a:
    if i < n:
        c.append(i)
    i += 1
print(c)