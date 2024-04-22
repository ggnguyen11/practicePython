# practicepython.org | exercise 26 | 04/18/2024
# part 2 of 4 of the tic tac toe series, to check winning conditions for a
# game of tic tac toe, positions represented w/ lists
# 0 - empty square, 1 - space occupied by player 1's move, 2 - player 2
# print whether there is a winner, and which player won, given a list of lists
# input is a 3x3 list of lists

# initializing lists for the 3 rows of the 3x3 board, and the board
top_row, mid_row, bot_row, board = [],[],[],[]

# iterating through each element of the row for player moves
print("\nPlease provide a game state to evaluate.")
for i in range(3):
    top_row.append(int(input("\nEnter numbers for 1st row:\n" + \
                        "0 = unmarked " + "space, 1 = player 1 move, " + \
                            "2 = player 2 move\n\n")))
print("\n1st row:\n" + str(top_row))

for i in range(3):
    mid_row.append(int(input("\nEnter numbers for 2nd row:\n" + \
                        "0 = unmarked " + "space, 1 = player 1 move, " + \
                            "2 = player 2 move\n\n")))
print("\n2nd row:\n" + str(mid_row))

for i in range(3):
    bot_row.append(int(input("\nEnter numbers for last row:\n" + \
                        "0 = unmarked " + "space, 1 = player 1 move, " + \
                            "2 = player 2 move\n\n")))
print("\nLast row:\n" + str(bot_row))

# appending all rows from top to bottom to board, a matrix
board.append(top_row)
board.append(mid_row)
board.append(bot_row)

# function to evaluate matrice for their tic tac toe game state
def move_checker(game_state):
# assessing winning positions
    if (game_state[0][0] == 1 and game_state[0][1] == 1 and \
    game_state[0][2] == 1) or (game_state[0][0] == 1 and \
    game_state[1][0] == 1 and game_state[2][0] == 1) or \
    (game_state[0][0] == 1 and game_state[1][1] == 1 and \
    game_state[2][2] == 1) or (game_state[0][2] == 1 and \
    game_state[1][2] == 1 and game_state[2][2] == 1) or \
    (game_state[2][0] == 1 and game_state[2][1] == 1 and \
    game_state[2][2] == 1) or (game_state[0][2] == 1 and \
    game_state[1][1] == 1 and game_state[2][0] == 1) or \
    (game_state[0][1] == 1 and game_state[1][1] == 1 and \
    game_state[2][1] == 1) or (game_state[1][0] == 1 and \
    game_state[1][1] == 1 and game_state[1][2]) == 1:
        print("\nPlayer 1 wins!\n\n")
    elif (game_state[0][0] == 2 and game_state[0][1] == 2 and \
    game_state[0][2] == 2) or (game_state[0][0] == 2 and \
    game_state[1][0] == 2 and game_state[2][0] == 2) or \
    (game_state[0][0] == 2 and game_state[1][1] == 2 and \
    game_state[2][2] == 2) or (game_state[0][2] == 2 and \
    game_state[1][2] == 2 and game_state[2][2] == 2) or \
    (game_state[2][0] == 2 and game_state[2][1] == 2 and \
    game_state[2][2] == 2) or (game_state[0][2] == 2 and \
    game_state[1][1] == 2 and game_state[2][0] == 2) or \
    (game_state[0][1] == 2 and game_state[1][1] == 2 and \
    game_state[2][1] == 2) or (game_state[1][0] == 2 and \
    game_state[1][1] == 2 and game_state[1][2]) == 2:
        print("\nPlayer 2 wins!\n\n")
    else:
        print("\nNo winners for this game state.\n\n")
# display board in matrix form
    print(top_row)
    print(mid_row)
    print(bot_row)

move_checker(board)