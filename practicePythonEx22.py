# practicepython.org | exercise 22 | 03/18/2024
# given a .txt file (saved as ex22Base.txt) w/ a list of a bunch of names,
# count the instances of each name and print the results to the screen.
# extra: using a different .txt file (saved as ex22Extra.txt), count how
# many of each "category" of each image there are. +string parsing

# initializing names list and nameCount dictionary to be populated with file
# data and number of name instances
names = []
nameCount = {"Darth":0, "Luke":0, "Lea":0}
Darth = Luke = Lea = 0
# opening a file for reading; like opening for writing but w/ different flag
with open('ex22Base.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        if line.strip("\n") not in names:
            names.append(line.strip("\n"))
# conditionals to increment name counters for each unique instance
        if line.strip("\n") == "Darth":
            Darth += 1
        elif line.strip("\n") == "Luke":
            Luke += 1
        elif line.strip("\n") == "Lea":
            Lea += 1
        line = open_file.readline()

# assigning values of name counters to dictionary pairs
nameCount["Darth"], nameCount["Luke"], nameCount["Lea"] = Darth, Luke, Lea

print(nameCount)

# extra 