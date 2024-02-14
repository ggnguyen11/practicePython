# practicepython.org | exercise 19 | 02/14/2024
# prompt: using requests and BeautifulSoup libraries print to the screen the
# full text of the article on this website:
#http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
# article is multiple pages -- print out full article to screen
import requests
from bs4 import BeautifulSoup

# storing website's HTML in a variable, enclosing within parentheses instead
# of using \ for line continuation
url = ('http://www.vanityfair.com/society/2014/06/'
       'monica-lewinsky-humiliation-culture')

# response object that stores server's response to HTTP request
r = requests.get(url)

# variable containing HTML content
r_html = r.text
soup = BeautifulSoup(r_html)

for container in soup.find_all(class_="body__inner-container"):
    if container.p:
        print(container.p.text.replace("\n", " ").strip())
    else:
        print(container.contents[0].strip())

# putting on hold as this challenege was developed for the Internet in 2014
# moving on to other exercises to avoid meaningless roadblocks