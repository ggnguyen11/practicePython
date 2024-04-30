# practicepython.org | exercise 29 | 04/26/2024
# write a program using components from previous parts of ttt to create a full
# tic tac toe game; keep track of who won and stop game when there are no more
# moves left
# bonus: ask players if they want to play again and keep a running tally of
# which player has won more

# function to reset game state
def clear_board():
# modifying global variable game matrix
    global game
    game = [[' ', ' ', ' '], \
            [' ', ' ', ' '], \
            [' ', ' ', ' ']]
    return(game)

# clean game state matrix
game = clear_board()

# initializing win count
p1_wins = 0
p2_wins = 0

# game start
print("\nLet's play Tic Tac Toe!\nPlayer 1 (X) - your move.\n\n" + \
        "Please enter the coordinates of the space where you'd like to " + \
        "place a move.\n(Format: (row,col) with range (1,1) to (3,3))")

# board() function from exercise 24, refactored to show active moves
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

# function to replay game
def repeat_game(winner):
    repeat = input("The game has ended. " + winner + " wins!\n\nPlayer 1 " + \
        "wins: " + str(p1_wins) + "\nPlayer 2 wins: " + str(p2_wins) + \
        "\n\nWould you like to play again? (Y/N)\n")
    # repeat game
    if repeat.lower() == 'y':
        clear_board()
        player_moves('X')
        return repeat.lower()
    elif repeat.lower() == 'n':
        print("Score:\nPlayer 1: " + str(p1_wins) + "\nPlayer 2: " + \
        str(p2_wins))
        return repeat.lower()

# player_moves() function from exercise 27, to determine placement of moves
def player_moves(player):
    while ' ' in game[0] or ' ' in game[1] or ' ' in game[2]:
# win conditions from ex26, modified
        if (game[0][0] == 'X' and game[0][1] == 'X' and \
        game[0][2] == 'X') or (game[0][0] == 'X' and \
        game[1][0] == 'X' and game[2][0] == 'X') or \
        (game[0][0] == 'X' and game[1][1] == 'X' and \
        game[2][2] == 'X') or (game[0][2] == 'X' and \
        game[1][2] == 'X' and game[2][2] == 'X') or \
        (game[2][0] == 'X' and game[2][1] == 'X' and \
        game[2][2] == 'X') or (game[0][2] == 'X' and \
        game[1][1] == 'X' and game[2][0] == 'X') or \
        (game[0][1] == 'X' and game[1][1] == 'X' and \
        game[2][1] == 'X') or (game[1][0] == 'X' and \
        game[1][1] == 'X' and game[1][2]) == 'X':
            winner = 'Player 1'
            return winner
        elif (game[0][0] == 'O' and game[0][1] == 'O' and \
        game[0][2] == 'O') or (game[0][0] == 'O' and \
        game[1][0] == 'O' and game[2][0] == 'O') or \
        (game[0][0] == 'O' and game[1][1] == 'O' and \
        game[2][2] == 'O') or (game[0][2] == 'O' and \
        game[1][2] == 'O' and game[2][2] == 'O') or \
        (game[2][0] == 'O' and game[2][1] == 'O' and \
        game[2][2] == 'O') or (game[0][2] == 'O' and \
        game[1][1] == 'O' and game[2][0] == 'O') or \
        (game[0][1] == 'O' and game[1][1] == 'O' and \
        game[2][1] == 'O') or (game[1][0] == 'O' and \
        game[1][1] == 'O' and game[1][2]) == 'O':
            winner = 'Player 2'
            return winner
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
    # when all spaces are occupied, but there are no winners
    replay = input("There are no winners for this game state.\n\n" + \
    "Player 1 wins: " + str(p1_wins) + "\nPlayer 2 wins: " + str(p2_wins) + \
    "\n\nPlay again? (Y/N)\n")
    if replay.lower() == 'y':
        clear_board()
        player_moves('X')
    elif replay.lower() == 'n':
        print("\nGame over!")
# terminates execution of program
        exit()

game_winner = player_moves('X')

# updating win count outside of while loop when repeat_game() returns 'n'
if game_winner == 'Player 1':
    p1_wins += 1
elif game_winner == 'Player 2':
    p2_wins += 1
# repeating game so long as repeat_game() function returns 'y'
while repeat_game(game_winner) == 'y':
    if game_winner == 'Player 1':
        p1_wins += 1
        repeat_game(game_winner)
    elif game_winner == 'Player 2':
        p2_wins += 1
        repeat_game(game_winner)
    else:
        print("Game over!\n")
        break