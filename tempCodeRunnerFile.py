import random

def gen_answer():
    numstr = ''
    for i in range(4):
        numstr += str(random.randint(0, 9))
    return numstr

answer = gen_answer()
guess = input("gimme number: \n")

def num_bulls(guess):
    bulls = 0
    guess_str = str(guess)
    for i in guess_str:
        if guess_str[i] not in answer:
            print("no")
        while guess_str[i] != answer[i]:
            if guess_str[i] in answer:
                bulls