# placeholder file to hold code that may be cut/repasted
def num_bulls(guess):
    bulls = 0
    guess_str = str(guess)
# checking for element within string, but not match case for exact position
    if (guess_str[0] in answer and guess_str[0] != answer[0]) or \
        (guess_str[1] in answer and guess_str[1] != answer[1]) or \
            (guess_str[2] in answer and guess_str[2] != answer[2]) or \
                (guess_str[3] in answer and guess_str[3] != answer[3]):
        bulls = 1
# checking for elements within string: 1st and 2nd, 1st and 3rd, 1st and 4th,
# 2nd and 3rd, 2nd and 4th, 3rd and 4th
    elif ((guess_str[0] in answer and guess_str[0] != answer[0]) and \
        (guess_str[1] in answer and guess_str[1] != answer[1])) or \
            ((guess_str[0] in answer and guess_str[0] != answer[0]) and \
        (guess_str[2] in answer and guess_str[2] != answer[2])) or \
            ((guess_str[0] in answer and guess_str[0] != answer[0]) and \
        (guess_str[3] in answer and guess_str[3] != answer[3])) or \
            ((guess_str[1] in answer and guess_str[1] != answer[1]) and \
        (guess_str[2] in answer and guess_str[2] != answer[1])) or \
            ((guess_str[1] in answer and guess_str[1] != answer[1]) and \
        (guess_str[3] in answer and guess_str[3] != answer[3])) or \
            ((guess_str[2] in answer and guess_str[2] != answer[2]) and \
        (guess_str[3] in answer and guess_str[3] != answer[3])):
        bulls = 2
# checking for elements within string: 1st + 2nd + 3rd, 1st + 2nd + 4th,
# 1st + 3rd + 4th, 2nd + 3rd + 4th
    elif ((guess_str[0] in answer and guess_str[0] != answer[0]) and \
            (guess_str[1] in answer and guess_str[1] != answer[1]) and \
            (guess_str[2] in answer and guess_str[2] != answer[2])) or \
            ((guess_str[0] in answer and guess_str[0] != answer[0]) and \
            (guess_str[1] in answer and guess_str[1] != answer[1]) and \
            (guess_str[3] in answer and guess_str[3] != answer[3])) or \
            ((guess_str[0] in answer and guess_str[0] != answer[0]) and \
            (guess_str[2] in answer and guess_str[2] != answer[2]) and \
            (guess_str[3] in answer and guess_str[3] != answer[3])) or \
            ((guess_str[1] in answer and guess_str[1] != answer[1]) and \
            (guess_str[2] in answer and guess_str[2] != answer[2]) and \
            (guess_str[3] in answer and guess_str[3] != answer[3])):
        bulls = 3
    elif (guess_str[0] in answer and guess_str[0] != answer[0]) and \
    (guess_str[1] in answer and guess_str[1] != answer[1]) and \
    (guess_str[2] in answer and guess_str[2] != answer[2]) and \
    (guess_str[3] in answer and guess_str[3] != answer[3]):
        bulls = 4
    return bulls

# test code