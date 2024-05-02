# practicepython.org | exercise 30 | 05/01/2024
# part 1/3 of hangman series: write function that picks random word from the
# SOWPODS dictionary. Each line in file contains a single word.

import random

scrabble = []

with open('sowpods.txt', 'r') as f:
    line = f.readline()
    while line:
        scrabble.append(line)
        line = f.readline()

print('\n' + random.choice(scrabble))