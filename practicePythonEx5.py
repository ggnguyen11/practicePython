# practicepython.org | exercise 5 | 01/26/2024
# prompt: take two lists, print their common elements (w/o dupes) and make
# sure that it works for two lists of different sizes
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

if a > b:
    longerlist = a
    otherlist = b
elif b > a:
    longerlist = b
    otherlist = a

for i in range(len(longerlist)):
    if longerlist[i] in otherlist and longerlist[i] not in c:
        c.append(longerlist[i])
i += 1

print(c)

# extra 1: randomly generate two lists to test
d = []
e = []
f = []
for i in range(random.randint(1, 20)):
    d.append(random.randint(1,100))
i += 1
print(d)

for i in range(random.randint(1, 20)):
    e.append(random.randint(1,100))
i += 1
print(e)

if d > e:
    longerlist2 = d
    otherlist2 = e
elif e > d:
    longerlist2 = e
    otherlist2 = d

for i in range(len(longerlist2)):
    if longerlist2[i] in otherlist2 and longerlist2[i] not in f:
        f.append(longerlist2[i])
i += 1

print(f)

# extra 2: write this in one line of python
print(set(a).intersection(b))