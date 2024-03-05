# using code from ex17 solution, print the results to a txt file instead of
# printing to the screen; make up a name for the file you are saving to
# extra: ask user to specify name of the output file that will be saved

# solution from ex17 to parse website
import requests
import re

from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
pattern = re.compile(r'indicate-hover')

matchedElements = soup.find_all(attrs={'class': pattern})
for element in matchedElements:
    print(element)
