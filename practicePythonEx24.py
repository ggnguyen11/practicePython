# practicepython.org | exercise 24 | 04/12/2024
# "pt 1 of 4 in tic tac toe" series, ask user for the size of the game board
# and print that to the screen, using functions**

# function to display the graphics of the matrix, using number of rows and
# columns as inputs, initializing horizontal and vertical with the starting
# symbols at the far left of the matrix
def board(rows, columns):
    horizontal = ' '
    vertical = '|'
# += statement to append to the end of string
    for n in range(columns):
        horizontal += '--- '
    for m in range(columns):
        vertical += '   |'
    for m in range(rows):
        print(horizontal)
        print(vertical)
    print(horizontal)

# function to obtain dimensions of the game board to pipe into the board()
# function above
def dimensions():
    rows = int(input("Let's make a game board!\n" + "Please specify its "\
        + "dimensions.\n" + "Rows: "))
    columns = int(input("Columns: "))
    repeat = input("Please confirm if these are the correct dimensions:\n" + \
        "\'y\' or \'n\'" + "\n" + str(rows) + "x" + str(columns) + "\n")
    if repeat.lower() == 'y':
        board(rows, columns)
    elif repeat.lower() == 'n':
        return dimensions()
    else:
        print("Please enter either \'y\' or \'n\' to confirm the dimensions")
        return dimensions()

dimensions()

# simplified solution from practicepython.org
#def print_horiz_line():
#    print(" ---" * board_size)

#def print_vert_line():
#    print("|   " * (board_size + 1))

#if __name__ == "__main__":
#    board_size = int(input("What size of game board? "))

#for index in range(board_size):
#    print_horiz_line()
#    print_vert_line()
#print_horiz_line()