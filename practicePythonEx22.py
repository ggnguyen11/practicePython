# practicepython.org | exercise 22 | 03/18/2024
# given a .txt file (saved as ex22Base.txt) w/ a list of a bunch of names,
# count the instances of each name and print the results to the screen.
# extra: using a different .txt file (saved as ex22Extra.txt), count how
# many of each "category" of each image there are. +string parsing

# opening a file for reading; like opening for writing but w/ different flag
with open('nytimesHeadings.txt', 'r') as open_file:
    content = open_file.read()