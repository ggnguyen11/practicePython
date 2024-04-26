# practicepython.org | exercise 29 | 04/26/2024
# write a program using components from previous parts of ttt to create a full
# tic tac toe game; keep track of who won and stop game when there are no more
# moves left
# bonus: ask players if they want to play again and keep a running tally of
# which player has won more

# board function from exercise 24
def board(rows, columns):
    horizontal = ' '
    vertical = '|'
    for n in range(columns):
        horizontal += '--- '
    for m in range(columns):
        vertical += '   |'
    for m in range(rows):
        print(horizontal)
        print(vertical)
    print(horizontal)

board(3, 3)