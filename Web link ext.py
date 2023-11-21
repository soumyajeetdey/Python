'''
#########################################################################
# web scraping

write a program to read https://www.google.com/ and display all the
available links in that wegpage

output :
https://mail.google.com/mail/&ogbl
https://www.google.com/imghp?hl=en&ogbl
https://www.google.com/?authuser=0
..
..

'''
url = 'https://www.google.com/'

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request("https://www.google.com/")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)

