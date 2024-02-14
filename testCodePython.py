# test
# def num_cows(guess):
#     cows = 0
#     guess_str = str(guess)
# # conditional for single match instance for 1st, 2nd, 3rd or 4th place
#     if (guess_str[0] == answer[0] and guess_str[1] != answer[1] and \
#     guess_str[2] != answer[2] and guess_str[3] != answer[3]) or \
#         (guess_str[1] == answer[1] and guess_str[0] != answer[0] and \
#             guess_str[2] != answer[2] and guess_str[3] != answer[3]) or \
#             (guess_str[2] == answer[2] and guess_str[0] != answer[0] and \
#     guess_str[1] != answer[1] and guess_str[3] != answer[3]) or \
#         (guess_str[3] == answer[3] and guess_str[0] != answer[0] and \
#     guess_str[1] != answer[1] and guess_str[2] != answer[2]):
#         cows = 1
# # conditional for double match instance for 1st + 2nd, 1st + 3rd, 1st + 4th,
# # 2nd + 3rd, 2nd + 4th, 3rd + 4th places
#     elif (guess_str[0] == answer[0] and guess_str[1] == answer[1] and \
#         guess_str[2] != answer[2] and guess_str[3] != answer[3]) or \
#             (guess_str[0] == answer[0] and guess_str[2] == answer[2] and \
#         guess_str[1] != answer[1] and guess_str[3] != answer[3]) or \
#             (guess_str[0] == answer[0] and guess_str[3] == answer[3] and \
#         guess_str[0] != answer[0] and guess_str[2] != answer[2]) or \
#             (guess_str[1] == answer[1] and guess_str[2] == answer[2] and \
#         guess_str[0] != answer[0] and guess_str[3] != answer[3]) or \
#             (guess_str[1] == answer[1] and guess_str[3] == answer[3] and \
#         guess_str[0] != answer[0] and guess_str[2] != answer[2]) or \
#             (guess_str[2] == answer[2] and guess_str[3] == answer[3] and \
#         guess_str[0] != answer[0] and guess_str[1] != answer[1]):
#         cows = 2
# # conditional for triple match instance for 1st + 2nd + 3rd, 1st + 2nd + 4th,
# # 1st + 3rd + 4th, 2nd + 3rd + 4th
#     elif (guess_str[0] == answer[0] and guess_str[1] == answer[1] and \
#         guess_str[2] == answer[2] and guess_str[3] != answer[3]) or \
#             (guess_str[0] == answer[0] and guess_str[1] == answer[1] and \
#         guess_str[3] == answer[3] and guess_str[2] != answer[2]) or \
#             (guess_str[0] == answer[0] and guess_str[2] == answer[2] and \
#         guess_str[3] == answer[3] and guess_str[1] != answer[1]) or \
#             (guess_str[1] == answer[1] and guess_str[2] == answer[2] and \
#         guess_str[3] == answer[3] and guess_str[0] != answer[0]):
#         cows = 3
#     elif guess_str[0] == answer[0] and guess_str[1] == answer[1] and \
#         guess_str[2] == answer[2] and guess_str[3] == answer[3]:
#         cows = 4
#     return cows
import random

def gen_answer():
    numstr = ''
    for i in range(4):
        numstr += str(random.randint(0, 9))
    return numstr

answer = gen_answer()
print(answer)
guess = input("gimme number: \n")

def get_cowsnbulls(guess):
    bulls = 0
    cows = 0
    i = 0
    guess_str = str(guess)
    while i < 4:
        if guess_str[i] == answer[i]:
            cows += 1
        elif guess_str[i] in answer:
            bulls += 1
        i += 1
    return cows, bulls

num_bulls(guess)