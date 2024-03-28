# practicepython.org | exercise 22 | 03/18/2024
# given a .txt file (saved as ex22Base.txt) w/ a list of a bunch of names,
# count the instances of each name and print the results to the screen.
# extra: using a different .txt file (saved as ex22Extra.txt), count how
# many of each "category" of each image there are. +string parsing

names = []
# opening a file for reading; like opening for writing but w/ different flag
with open('ex22Base.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
#        print(line)
        if line not in names:
            names.append(line.strip("\n"))
        line = open_file.readline()
        
uniqueNames = set(names)

dictLength = len(uniqueNames)

while dictLength != -1:
    nameCount = {uniqueNames[dictLength - 1]:[], uniqueNames[dictLength - 2]:\
        [], uniqueNames[dictLength - 3]:[]}

print(nameCount)
#for num in dictLength:
#    print(num)
    
#for name in uniqueNames:
#    nameCount[name].append(name)

#print(nameCount)