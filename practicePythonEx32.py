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

# function to clear and replay hangman game
def restart(replay):
# global variables to be reinitialized upon replay
    global correctLetters, guessedLetters, bar, count, sampleWord, letters
    if replay == 'y':
        correctLetters = []
        guessedLetters = []
        bar = []
        count = 0
# reloading game state with new word
        sampleWord = choose_word('sowpods.txt')
        letters = speller(sampleWord)
        bar = guess_bar(sampleWord)
        clear_hangman()
        matcher(count)
    else:
        return replay

# checks for guesses and occupied spaces
def matcher(count):
    while '_' in bar:
        #print("Count: " + str(count) + '\n')
        guess = input("Please guess a letter:\n").upper()
# game over condition
        if count == 5 and guess not in correctLetters and guess not in \
        guessedLetters:
            count += 1
            print("Maximum amount of guesses exceeded. Game over!")
# hangman() for visualization
            hangman(count)
            print("The correct word was: " + sampleWord)
# restart function
            replay = input("Would you like to play again? (Y/N)\n").lower()
            restart(replay)
            return count
        elif guess in correctLetters and guess not in guessedLetters:
# 6 - count for remaining guesses until game over
            guessedLetters.append(guess)
            #print("Chances: " + str(6 - count))
            print("Guessed letters:\n" + str(guessedLetters))
            hangman(count)
# replaces bar space with letter
            printBar(guess)
        elif guess in guessedLetters:
            print("That letter has already been guessed.\n" + "Chances: " + \
            str(6 - count))
            print("Guessed letters:\n" + str(guessedLetters))
            hangman(count)
            print(bar)
            return matcher(count)
        elif guess not in correctLetters and guess not in guessedLetters:
            count += 1
            guessedLetters.append(guess)
            #print("Chances: " + str(6 - count))
            print("Guessed letters:\n" + str(guessedLetters))
            hangman(count)
            print(bar)
# while all spaces are occupied
    print("Congratulations! You guessed the correct word with " + \
    str(6 - count) + " guesses remaining.")
    print("The correct word was: " + sampleWord)
    hangman(count)
# restart function
    replay = input("Would you like to play again? (Y/N)\n").lower()
    restart(replay)
    return count

# checks to see if guess is within the list of correct letters, then replaces
# empty space with the guess
def printBar(guess):
# range(len(correctLetters)) for index value instead of char value
    for char in range(len(correctLetters)):
# if value of guess is the correct letter for position of index, change space
        if correctLetters[char] == guess:
            bar[char] = guess
    print(bar)

# function to visualize hangman
body = [[' ', ' ', ' '], \
        [' ', ' ', ' '], \
        [' ', ' ', ' ']]

def hangman(count):
    global body
    if count == 0:
        pass
    elif count == 1:
        body[0][1] = 'O'
    elif count == 2:
        body[0][1] = 'O'
        body[1][1] = '|'
    elif count == 3:
        body[0][1] = 'O'
        body[1][1] = '|'
        body[1][0] = '/'
    elif count == 4:
        body[0][1] = 'O'
        body[1][1] = '|'
        body[1][0] = '/'
        body[1][2] = '\\'
    elif count == 5:
        body[0][1] = 'O'
        body[1][1] = '|'
        body[1][0] = '/'
        body[1][2] = '\\'
        body[2][0] = '/'
    elif count == 6:
        body[0][1] = 'O'
        body[1][1] = '|'
        body[1][0] = '/'
        body[1][2] = '\\'
        body[2][0] = '/'
        body[2][2] = '\\'
# setting up statements to print w/o brackets
    head = ' ' + str(body[0][1])
    torso = str(body[1][0]) + str(body[1][1]) + str(body[1][2])
    legs = str(body[2][0]) + ' ' + str(body[2][2])
    print(' | ', head, torso, legs, sep='\n')

# function to clear hangman()
def clear_hangman():
    global body
    body = [[' ', ' ', ' '], \
            [' ', ' ', ' '], \
            [' ', ' ', ' ']]

letters = speller(sampleWord)
bar = guess_bar(sampleWord)
matcher(count)

# simpler function for printing output bar - solution from practicepython.org

#def generate_word_string(word, letters_guessed):
#	output = []
#	for letter in word:
#		if letter in letters_guessed:
#			output.append(letter.upper())
#		else:
#			output.append("_")
#	return " ".join(output)

# conditionals for .add() & .remove() methods for sets instead of lists

#if guess in letters_to_guess:
#	letters_to_guess.remove(guess)
#	correct_letters_guessed.add(guess)
#else:
#	incorrect_letters_guessed.add(guess)
#	num_guesses += 1