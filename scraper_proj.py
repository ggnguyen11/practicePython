# test project for web scraper (05/26/2024)
# importing requests library 
import requests
# import re module for reg expressions
import re
# parsing string of HTML via BeautifulSoup
from bs4 import BeautifulSoup
# import pandas for data frames & readability
import pandas
# import lxml/ET for xpath parsing of XML structured documents
#import xml.etree.ElementTree as ET

# storing website HTML in a variable
# url = 'https://www.nba.com/game/min-vs-dal-0042300313/box-score'
url = input('Welcome to the NBA Box Score Scraper.\n\nPlease provide a' \
            ' url link:\n')

# variable for page element within HTML tree
# div = 'StatsTable_table__Ejk5X'
#div = input('\nPlease enter the page element for the box score section:\n' 
#            'String within <section class=\"\">\n')

# parses table for headers & rows
def table_parser(table):
# list of headers from parsing box score tables for table headers (th class)
    headers = [header.text.strip() for header in \
               table.find('thead').find_all('th')]
    rows = []
# list of table rows from parsing box score tables for data cell (td class)
    for tr in table.find('tbody').find_all('tr'):
        cells = [td.text.strip() for td in tr.find_all('td')]
        if cells:
            rows.append(cells)
    return headers, rows

# sifts soup for box score tables
def box_tables(tables):
    box_scores = []
    for table in tables:
# assigns function return values to variables
        headers, rows = table_parser(table)
        box_scores.append((headers, rows))
    return box_scores

# function to parse box score data from given url
def box_data(url):
# response object containing server's response to HTTP request
    r = requests.get(url)
    r_html = r.text
# parsing HTML content of object for text, default 'html.parser' to clear warning
    soup = BeautifulSoup(r_html, 'html.parser')
# parsing XML content
    #root = ET.fromstring(r_html)
# compiles regex pattern into object for use in matching operations
    #pattern = re.compile(r'StatsTable_container___qPry')
# finds all box score tables w/ class table from soup object
    #boxes = soup.find_all(attrs={'class': pattern})
    #for box in boxes:
    #    print(box)
    #box_score = box_tables(tables)
    #return tables, box_score
    #headers = [soup.text.strip() for header in \
    #           soup.find('thead').find_all('th')]
    #for table in root.findall('tbody'):
    #    row = table.find('tr').text
    #    col = table.find('td').text
    #    data = table.find('a').text
    #    print(f'Player: {row}, Stat: {col}, Data: {data}')
    #print(root)
    print(soup)

box_data(url)