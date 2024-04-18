# practicepython.org | exercise 26 | 04/18/2024
# part 2 of 4 of the tic tac toe series, to check winning conditions for a
# game of tic tac toe, positions represented w/ lists
# 0 - empty square, 1 - space occupied by player 1's move, 2 - player 2
# print whether there is a winner, and which player won, given a list of lists
# input is a 3x3 list of lists
board = input("Please provide a game state to evaluate:\n" + \
    "Format: [[n, n, n], [n, n, n], [n, n, n]]\n0 = unmarked " + \
        "space, 1 = player 1 move, 2 = player 2 move\n")

print(board)