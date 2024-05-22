# practicepython.org | exercise 33 | 05/21/2024
# pt 1/4 of birthday data series: create a dictionary of names and birthdays
# program asks user to enter a name and returns birthday of that person
birthdays = {'Abe':'05/19/1998', 'Reggie':'06/25/2000', 'Gia':'05/27/1963', \
             'Aria':'2/20/1970', 'Ryan':'11/09/2010', 'Ian':'05/31/1997'}

def birthday_dictionary():
# .format() method to cast data types into strings, in place of {}
    name = input('Welcome to the birthday dictionary. Whose birthday are' + \
    ' you searching for?\n{}\n{}\n{}\n{}\n{}\n{}'.format('Abe', 'Reggie', \
    'Gia', 'Aria', 'Ryan', 'Ian\n\n'))
    print('{}\'s birthday is on {}.'.format(name.capitalize(), \
    birthdays[name.capitalize()]))

birthday_dictionary()