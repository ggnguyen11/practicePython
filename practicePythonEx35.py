# practicepython.org | exercise 35 | 05/27/2024
# pt 3/4 of birthday data series: load JSON file from disk, extract months of
# all birthdays and count how many people have a birthday in each month

# output should be: {
#	"May": 3,
#	"November": 2,
#	"December": 1
#}
import json

# importing Counter (takes list and counts its elements)
from collections import Counter

#birthdays = {'Abe':'05/19/1998', 'Reggie':'06/25/2000', 'Gia':'05/27/1963', \
#             'Aria':'2/20/1970', 'Ryan':'11/09/2010', 'Ian':'05/31/1997'}

month_values = {'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', \
                '06':'Jun', '07':'Jul', '08':'Aug', '09':'Sep', '10':'Oct', \
                '11':'Nov', '12':'Dec'}

# load JSON file
def load_json(file):
    with open(file, 'r') as f:
        info = json.load(f)
# initializing lists to store components of json file
    keys = []
    values = []
    months = []
    for key in info:
# storing individuals' names
        keys.append(key)
# storing individuals' birthdays
        values.append(info[key])
    print(f"Keys: {keys}\nValues: {values}")
    for value in values:
# stores the first two digits denoting the month for mm/dd/yyyy
        months.append(value[:2])
    print(f"Months: {months}")
# for index in length of months, assign the value associated w/ the 2-digit
# month identifier to that element index
    for month in range(len(months)):
        months[month] = month_values[months[month]]
    return months

# function to use Counter data structure
def month_counter(list):
    c = Counter(list)
    for i in c:
        print(f"{i}: {c[i]}")

#load_json('info.json')

month_counter(load_json("info.json"))