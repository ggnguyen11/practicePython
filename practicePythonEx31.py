# practicepython.org | exercise 31 | 05/01/2024
# pt 2/3 of hangman: write logic that asks player to guess a letter and
# displays letters in the clue word that were guessed correctly
# stop game when word is guessed

# extra: keep track of letters guessed and display a different message
# for duplicate guesses

sample = 'EVAPORATE'
# initializing list for guesses
correctLetters = []
guessedLetters = []
count = 0

# takes the word and appends its letters to a list
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
def matcher(count):
    while '_' in bar:
        guess = input("Please guess a letter:\n").upper()
        print(guess)
        if guess in correctLetters and guess not in guessedLetters:
            count += 1
            guessedLetters.append(guess)
            print("\nGuesses: " + str(count) + "\n")
            print("Guessed letters:\n" + str(guessedLetters) + "\n")
# replaces bar space with letter
            printBar(guess)
        elif guess in guessedLetters:
            count += 1
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
    print("Congratulations! You guessed the correct word in " + \
    str(count) + " guesses.")
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

letters = speller(sample)
bar = guess_bar(sample)
matcher(count)