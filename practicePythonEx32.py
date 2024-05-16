# practicepython.org | exercise 32 | 05/16/2024
# pt 3/3 of the hangman series, finish programming the game of hangman, using
# parts 1 & 2 of the series as reference

# only let the user guess 6 times & print remaining guesses
# keep track of guessed letters & let user keep guessing if they guess a
# letter they've already guessed

# optional: when the player wins/loses, let them start a new game
# instead of telling the user the remaining guesses, show a visual
# representation of the hanged man

# pt 1/3, which chooses a random word from the SOWPODS dictionary
import random

def choose_word(textFile):
    word = []
    with open(textFile, 'r') as f:
        line = f.readline()
        while line:
            word.append(line)
            line = f.readline()
    return random.choice(word)

# pt 2/3, which takes the chosen word above and uses it for the hangman game
# stores output in variable sample for use in other functions
sampleWord = choose_word('sowpods.txt')

# initializing variables for hangman game
correctLetters = []
guessedLetters = []
count = 0

# takes word and appends its letters to a list
def speller(word):
    length = len(word)
    for char in range(length):
        correctLetters.append(word[char])

# displays missing spaces for each character in the given word
def guess_bar(word):
    bar = []
    for char in word:
        bar.append('_')
    return bar

# checks for guesses and occupied spaces