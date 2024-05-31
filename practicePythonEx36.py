# practicepython.org | exercise 36 | 05/31/2024
# pt 4/4 of birthday data series: use bokeh py lib to plot histogram of which
# months scientists have birthdays in, using given JSON file; parse months

# importing Counter & JSON for parsing
from collections import Counter
import json

# bokeh plotting library for visualizations
import bokeh

# function to read JSON
def read_json(file):
    with open(file, 'r') as f:
        info = json.load(f)
    keys = []
    values = []
    for key in info:
        keys.append(key)
        values.append(info[key])
    print(values)
    
read_json('scientists_bday.json')