# practicepython.org | exercise 6 | 01/27/2024
# prompt: ask user for string, print whether string is palindrome or not
# does it read the same forwards and backwards?
stringtest = input("Please give me a string: ")

# reverses string
backword = stringtest[::-1]

# conditional
if backword == stringtest:
    print("Your string is a palindrome!")
# alternative solution: use else instead of elif
elif backword != stringtest:
    print("Your string is not a palindrome!")

