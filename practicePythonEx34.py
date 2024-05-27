# practicepython.org | exercise 34 | 05/27/2024
# modify program from pt 1/4 to load the birthday dict from a JSON file on
# disk rather than defining dictionary in program
# extra: ask user for another scientist's name and birthday to add to file

# built-in library for r/w JSON files
import json

# given json dictionary
personal_info = {
    "name": "Michelle",
    "has_a_dog": False
}

file = input("Please enter a .json file to read/modify:\n")

# function that adds requested text to existing file contents
def write_json(info, file):
    add = input("\nWhat would you like to add?\nFormat: {'key': 'value'}\n")
# seperate by newline
    info += f'\n{add}'
# opening file for writing
    with open(file, "w") as f:
        json.dump(info, f)
    print(info)

# function to view file contents & prompt for modification
def read_json(file):
# reading file as f object
    with open(file, "r") as f:
# deserialize json content into strings
        info = json.load(f)
        print(f'\n{info}')
    mod = input("\nWould you like to add to this file? (Y/N)\n").lower()
    if mod == 'y':
        write_json(info, file)
    else:
        return file

read_json(file)