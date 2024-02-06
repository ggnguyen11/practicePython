# practicepython.org | exercise 17 | 02/02/2024
# prompt: use BeautifulSoup and requests Python packages to print out a list
# of all the article titles on the New York Times homepage
# requests library for internet queries from python
import requests
# import re module for regular expressions
import re

# requesting website's HTML & storing in a variable
url = 'https://www.nytimes.com'

# response object that stores server's response to HTTP request
r = requests.get(url)
# HTML content stored in r_html variable
r_html = r.text

# to parse (read/interpret) string of HTML from requests
# use BeautifulSoup library
from bs4 import BeautifulSoup
# explicitly specifying the parser to get rid of 'GuessedAtParserWarning'
# message in console output
soup = BeautifulSoup(r_html, 'html.parser')
# find() method searches HTML tree for first occurrence of the specified
# element "<p>" w/ class
# compiles regex pattern into regex object for use w/ matching operations
# takes pattern as required argument -- the string to be matched in text
pattern = re.compile(r'indicate-hover')
# find method w/ regex pattern to search for elements matching a part of the
# specified class
# pass dictionary to the 'attrs' parameter, w/ key 'class' & value is compiled
# regex pattern
matchedElements = soup.find_all(attrs={'class': pattern})
for element in matchedElements:
    print(element)