# practicepython.org | exercise 36 | 05/31/2024
# pt 4/4 of birthday data series: use bokeh py lib to plot histogram of which
# months scientists have birthdays in, using given JSON file; parse months

# importing Counter & JSON for parsing
from collections import Counter
import json

# bokeh library for visualizations, need these 3 modules for plots to work
from bokeh.plotting import figure, show, output_file

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
    return values

# function to parse months from mm/dd/yyyy format
def parse_months(dates):
# initializing dictionary for mm: month key: value pairs
    month_values = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }
    months = []
    for month in dates:
# parsing mm value from mm/dd/yyyy
        id = month[:2]
        months.append(month_values[id])
    print(months)
    return months

# function to count instances of months within list
def month_counter(list):
    c = Counter(list)
    count = []
    for i in c:
# month: month count
        print(f"{i}: {c[i]}")
        count.append(c[i])
    return count

# function that uses bokeh to output plot based on inputs x, y
def plot_months(x, y):
# specifying output.html file
    output_file("plot.html")
# categorical, non-continuous variable
    x_categories = []
    y_values = []
    for month in x:
# for multiple counts of same month birthdates
        if month not in x_categories:
            x_categories.append(month)
        else:
            continue
    for count in y:
        y_values.append(count)
# passing x_range through figure() so bokeh draws categorical axis correctly
    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=0.5)
    show(p)

dates = read_json('scientists_bday.json')
months = parse_months(dates)
y = month_counter(months)
plot_months(months, y)