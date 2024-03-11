# using code from ex17 solution, print the results to a txt file instead of
# printing to the screen; make up a name for the file you are saving to
# extra: ask user to specify name of the output file that will be saved

# solution from ex17 to parse website
import requests
from bs4 import BeautifulSoup

# storing website's HTML in a variable
url = 'https://www.nytimes.com'

# response object that store's server's response to HTTP request
r = requests.get(url)

# r.text w/ HTML content to be parsed by BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

def headingPrinter(stew):
# find all matches w/ specified string pattern, iterate through each
# and print to line, stripping newlines and whitespaces
    for heading in stew.find_all(class_="indicate-hover"):
        if heading.a:
            print(heading.a.text.replace("\n", " ").strip())
        else:
            print(heading.contents[0].strip())

finalSoup = headingPrinter(soup)

print(finalSoup)