# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:11:07 2019

@author: Brian
"""

"Import dependencies"
from bs4 import BeautifulSoup
import requests

"Get page from url"
"""
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
"""
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

"Open page with soup"
soup = BeautifulSoup(page.content, 'html.parser')

"""
"Print formatted HTML page"
print(soup.prettify())

"Show all types of tags"
list(soup.children)

"Show types of elements"
[type(item) for item in list(soup.children)]

"Show all children with html tag"
html = list(soup.children)[2]

list(html.children)

"Isolate body inside html tag"
body = list(html.children)[3]

"Isolate text inside body"
p = list(body.children)[1]
"""

soup.find_all('p', class_='outer-text')
soup.find_all('p')[0].get_text()
soup.find_all(id="first")