# practicepython.org | exercise 4 | 01/25/2024
# prompt: ask user for number, print list of all divisors of that number
n = int(input("Please enter a number: "))
divisors = []

# loop for range (1, n + 1), as ending index is noninclusive
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
    elif n % i != 0:
        continue
    i += 1
print(divisors)