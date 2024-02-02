# practicepython.org | exercise 17 | 02/02/2024
# prompt: use BeautifulSoup and requests Python packages to print out a list
# of all the article titles on the New York Times homepage
# requests library for internet queries from python
import requests

# requesting website's HTML & storing in a variable
url = 'nytimes.com'
r = requests.get(url)
r_html = r.text

# to parse (read/interpret) string of HTML from requests
# use BeautifulSoup library
from bs4 import BeautifulSoup
soup = BeautifulSoup(r_html)
title = soup.find('span', 'articletitle').string