# practicepython.org | exercise 31 | 05/01/2024
# pt 2/3 of hangman: write logic that asks player to guess a letter and
# displays letters in the clue word that were guessed correctly
# stop game when word is guessed

# extra: keep track of letters guessed and display a different message
# for duplicate guesses

sample = 'EVAPORATE'

# takes the word and appends its characters to a list one by one
def speller(word):
    length = len(word)
    letters = []
    for char in range(length):
        letters.append(word[char])

# displays missing spaces for each character in the given word
def guess_bar(word):
    bar = [' ']
    for char in word:
        bar.append('_ ')
    print(bar)
    return bar

def matcher():
    pass

speller(sample)
guess_bar(sample)
# matcher(guess_bar(sample))