# with two .txt files containing numbers, find numbers that are overlapping
# one file contains all primes 1-1000 and the other w/ happy numbers 1-1000

prime_nums = []
happy_nums = []

with open('ex23Primes.txt', 'r') as primes:
    pline = primes.readline()
    while pline:
        pline.strip('\n')
# int conversion from string to allow for proper numeric sorting
        pline = int(pline)
        prime_nums.append(pline)
        pline = primes.readline()


with open('ex23Happy.txt', 'r') as happy:
    hline = happy.readline()
    while hline:
        hline.strip('\n')
        hline = int(hline)
        happy_nums.append(hline)
        hline = happy.readline()

# set().intersection() method to find all shared occurences across two lists
overlap = ((set(prime_nums)).intersection(happy_nums))

print(sorted(overlap))