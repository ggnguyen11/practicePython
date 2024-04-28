# practicepython.org | exercise 29 | 04/26/2024
# write a program using components from previous parts of ttt to create a full
# tic tac toe game; keep track of who won and stop game when there are no more
# moves left
# bonus: ask players if they want to play again and keep a running tally of
# which player has won more

# initial game state matrix
game = [[' ', ' ', ' '], \
        [' ', ' ', ' '], \
        [' ', ' ', ' ']]

# game start
print("\nLet's play Tic Tac Toe!\nPlayer 1 (X) - your move.\n\n" + \
        "Please enter the coordinates of the space where you'd like to " + \
        "place a move.\n(Format: (row,col) with range (1,1) to (3,3))")

# board() function from exercise 24, refactored
def board():
    print(' --- --- --- ')
    print('| '+ game[0][0] + ' |' + ' '+ game[0][1] + ' ' + '| '+ game[0][2] \
    + ' |')
    print(' --- --- --- ')
    print('| '+ game[1][0] + ' |' + ' '+ game[1][1] + ' ' + '| '+ game[1][2] \
    + ' |')
    print(' --- --- --- ')
    print('| '+ game[2][0] + ' |' + ' '+ game[2][1] + ' ' + '| '+ game[2][2] \
    + ' |')
    print(' --- --- --- ')

# player_moves() function from exercise 27, to determine placement of moves
def player_moves(player):
    while ' ' in game[0] or ' ' in game[1] or ' ' in game[2]:
        if player == 'X':
# splits coordinates by excluding the comma, storing the two numbers in a list
            move = input("\nPlayer 1's move:\n").split(',')
        elif player == 'O':
            move = input("\nPlayer 2's move:\n").split(',')
# checking to see if space in matrix is occupied
        if game[int(move[0]) - 1][int(move[1]) - 1] == 'X' or \
        game[int(move[0]) - 1][int(move[1]) - 1] == 'O':
            board()
            print("That space is currently occupied, please enter another" + \
                " set of coordinates.\n")
            return player_moves(player)
# if free space
        else:
            if player == 'X':
                game[int(move[0]) - 1][int(move[1]) - 1] = 'X'
                board()
                player_moves('O')
            elif player == 'O':
                game[int(move[0]) - 1][int(move[1]) - 1] = 'O'
                board()
                player_moves('X')
    # when all spaces are occupied
    print("The game has ended. Player " + "winner" + " wins!")

player_moves('X')