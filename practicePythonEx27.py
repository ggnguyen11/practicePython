# practicepython.org | exercise 27 | 04/25/2024
# pt 3/4 of tic tac toe series: for player 1 move = X, player 2 move = O,
# create a program to take user input (coordinate format: (row,col) and update
# the "server board" with the player's moves

# considerations: may want to have coordinates starting at (1, 1) for players
# that don't program (initializing at 0 may be a foreign concept)
# do not allow for moves to be places in an occupied space

print("\nLet's play Tic Tac Toe!\nPlayer 1 (X) - your move.\n\n" + \
        "Please enter the coordinates of the space where you'd like to " + \
        "place a move.\n(Format: (row,col) with range (1,1) to (3,3))")

# initializing variables
# initial game state
game = [[0, 0, 0], \
        [0, 0, 0], \
        [0, 0, 0]]

# function to visualize board
def board():
    print("\n")
    print(game[0])
    print(game[1])
    print(game[2])

# function to determine placement of moves, dependent on the player moving
def player_moves(player):
# conditional to test whether there is still an empty space in the matrix
    while 0 in game[0] or 0 in game[1] or 0 in game[2]:
        move = input("\nPlayer " + player + " move:\n").split(',')
# conditional to check for occupied spaces in matrix
        if game[int(move[0]) - 1][int(move[1]) - 1] == 'X' or \
        game[int(move[0]) - 1][int(move[1]) - 1] == 'O':
            board()
            print("That space is currently occupied, please enter another" + \
                " set of coordinates.\n")
            return player_moves(player)
        else:
            if player == 'X':
                game[int(move[0]) - 1][int(move[1]) - 1] = 'X'
                board()
# switches player for function call
                player_moves('O')
            elif player == 'O':
                game[int(move[0]) - 1][int(move[1]) - 1] = 'O'
                board()
                player_moves('X')

player_moves('X')