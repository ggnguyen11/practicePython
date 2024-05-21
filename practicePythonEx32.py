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

# appends list with all words within input .txt file, then uses
# random.choice() to pick a word from the list for hangman
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

def initialize():
    global correctLetters, guessedLetters, count, bar
    correctLetters = []
    guessedLetters = []
    count = 0
    bar = []

# takes word and appends its letters to a list
def speller(word):
    length = len(word)
    for char in range(length):
        correctLetters.append(word[char])

# displays missing spaces for each character in the given word
def guess_bar(word):
    bar = []
    for char in range(len(word) - 1):
        bar.append('_')
    return bar

# function to replay hangman
def restart(replay):
    if replay == 'y':
        initialize()
        sampleWord = choose_word('sowpods.txt')
        speller(sampleWord)
        guess_bar(sampleWord)
        matcher(0)
    else:
        return False

# checks for guesses and occupied spaces
def matcher(count):
# game over
    while '_' in bar:
        guess = input("Please guess a letter:\n").upper()
#        print(guess)
        if count == 5:
            print("Maximum amount of guesses exceeded. Game over!")
            replay = input("The word was: " + sampleWord + "\nWould you " + \
                            "like to play again? (Y/N)\n")
            restart(replay.lower())
        if guess in correctLetters and guess not in guessedLetters:
            count += 1
            guessedLetters.append(guess)
            print("\nGuesses: " + str(count) + "\n")
            print("Guessed letters:\n" + str(guessedLetters) + "\n")
# replaces bar space with letter
            printBar(guess)
        elif guess in guessedLetters:
            print("That letter has already been guessed.\n" + "Guesses: " + \
            str(count) + "\n")
            print("Guessed letters:\n" + str(guessedLetters) + "\n")
            print(bar)
            return matcher(count)
        elif guess not in correctLetters:
            count += 1
            guessedLetters.append(guess)
            print("\nGuesses: " + str(count) + "\n")
            print("Guessed letters:\n" + str(guessedLetters) + "\n")
            print(bar)
# while all spaces are occupied
    replay = input("Congratulations! You spelled the word in " + str(count) +\
          " guesses.\n\n" + "Would you like to play again? (Y/N)\n")
    print(sampleWord)
    restart(replay)
    return replay.lower()

# checks to see if guess is within the list of correct letters, then replaces
# empty space with the guess
def printBar(guess):
# range(len(correctLetters)) for index value instead of char value
    for char in range(len(correctLetters)):
# if value of guess is the correct letter for position of index, change space
        if correctLetters[char] == guess:
            bar[char] = guess
    print(bar)

letters = speller(sampleWord)
bar = guess_bar(sampleWord)
matcher(count)