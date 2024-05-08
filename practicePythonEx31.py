# practicepython.org | exercise 31 | 05/01/2024
# pt 2/3 of hangman: write logic that asks player to guess a letter and
# displays letters in the clue word that were guessed correctly
# stop game when word is guessed

# extra: keep track of letters guessed and display a different message
# for duplicate guesses

# notes: try to use a dictionary to store and access sample letters
# instead of unordered lists/sets

sample = 'EVAPORATE'
# initializing dictionary
letters = {}
# initializing list for guesses
correctLetters = []
guessedLetters = []
count = 0

# takes the word and appends the letter index:letter as a key:pair element
# to a dictionary 
def speller(word):
    length = len(word)
    for char in range(length):
        correctLetters.append(word[char])
        letters[char] = word[char]
#    print(letters)
    return letters

# displays missing spaces for each character in the given word
def guess_bar(word):
    bar = []
    for char in word:
        bar.append('_')
    return bar

# checks for guesses and occupied spaces
def matcher(count):
    while '_' in bar:
        guess = input("Please guess a letter:\n")
        guess = guess.upper()
        if guess in correctLetters and guess not in guessedLetters:
            count += 1
            guessedLetters.append(guess)
            print("Guesses: " + str(count))
# replaces bar space with letter
            printBar(guessedLetters)
        elif guess in guessedLetters:
            count += 1
            print("That letter has already been guessed.\n" + "Guesses: " + \
            str(count) + "\n")
            return matcher(count)

def printBar(guesses):
    for char in guesses:
        if guesses[char] in correctLetters:
            bar[char] = correctLetters[char]
    print(bar)

letters = speller(sample)

bar = guess_bar(sample)
matcher(count)