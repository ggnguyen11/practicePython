# practicepython.org | exercise 15 | 01/29/2024
# prompt: write program using functions that asks user for a long string
# containing multiple words, and returns that in backwards order

def reverser(string1):
# teststring.split(), w/ no arguments, splits strings by whitespace -> list
    reverse = string1.split()
# flips sequence of strings
    reverse = reverse[::-1]
# joins strings from list
    reverse = ' '.join(reverse)
    print(reverse)

# one-line solution:
# def reverser(string1):
#    return ' '.join(string1.split()[::-1])
    
reverser(input("Please give me a string to reverse: "))