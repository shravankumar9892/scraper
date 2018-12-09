# Web Scraping with BeautifulSoup

import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page.content) is similiar to resp.read() from urllib.request
# Here, page is the whole response object which has many attributes. 


soup = BeautifulSoup(page.content, 'html.parser') 
# Both will give the html code of the webpage
# print(soup.prettify())
# print(page.text)

# To find types of object in soup.children
# [type(item) for item in list(soup.children)]

html = list(soup.children)[2] # Got <html> from <page>
body = list(html.children)[3] # Got <body> from <html>
p = list(body.children)[1]     # Got <p> from <body>

# To get text from paragraph
print(p.get_text())


