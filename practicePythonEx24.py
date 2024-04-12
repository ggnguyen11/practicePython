# practicepython.org | exercise 24 | 04/12/2024
# "pt 1 of 4 in tic tac toe" series, ask user for the size of the game board
# and print that to the screen, using functions**

#print(" --- --- --- ")
#print("|   |   |   |")

def dimensions():
    rows = int(input("Let's make a game board!\n" + "Please specify its "\
        + "dimensions.\n" + "Rows: "))
    columns = int(input("Columns: "))
    repeat = input("Please confirm if these are the correct dimensions:\n" + \
        str(rows) + "x" + str(columns) + "\n")

def hori_lines(rows):
    pass

dimensions()