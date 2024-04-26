# practicepython.org | exercise 29 | 04/26/2024
# write a program using components from previous parts of ttt to create a full
# tic tac toe game; keep track of who won and stop game when there are no more
# moves left
# bonus: ask players if they want to play again and keep a running tally of
# which player has won more

# initial game state matrix
game = [[0, 0, 0], \
        [0, 0, 0], \
        [0, 0, 0]]

# game start
print("\nLet's play Tic Tac Toe!\nPlayer 1 (X) - your move.\n\n" + \
        "Please enter the coordinates of the space where you'd like to " + \
        "place a move.\n(Format: (row,col) with range (1,1) to (3,3))")

# board() function from exercise 24
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

# player_moves() function from exercise 27, to determine placement of moves
def player_moves(player):
    while 0 in game[0] or 0 in game[1] or 0 in game[2]:
        move = input("\nPlayer " + player + " move:\n").split(',')
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
                player_moves('O')
            elif player == 'O':
                game[int(move[0]) - 1][int(move[1]) - 1] = 'O'
                board()
                player_moves('X')

player_moves('X')
board(3, 3)