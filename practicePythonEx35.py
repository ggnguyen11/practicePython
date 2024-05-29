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

# ex use case
#sandwiches = ["ham", "cheese", "roast beef", "ham", "cheese", "roast beef", "ham"]
#c = Counter(sandwiches)

#birthdays = {'Abe':'05/19/1998', 'Reggie':'06/25/2000', 'Gia':'05/27/1963', \
#             'Aria':'2/20/1970', 'Ryan':'11/09/2010', 'Ian':'05/31/1997'}

# load JSON file
def load_json(file):
    with open(file, 'r') as f:
        info = json.load(f)
        print(f'\n{info}')