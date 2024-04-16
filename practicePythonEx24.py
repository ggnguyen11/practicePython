# practicepython.org | exercise 24 | 04/12/2024
# "pt 1 of 4 in tic tac toe" series, ask user for the size of the game board
# and print that to the screen, using functions**

#
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