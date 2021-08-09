#!/usr/bin/python3                                    
# here is a she-bang for linux OS

# Here we search in the site using requests and print the results of the first page.

import requests
from bs4 import BeautifulSoup
import re             # Using re for Multi-word searches.


print('Hello body , welcome!','\n')
inp = input('What are you looking for?')

# If there is space in the input, we set + to instead.
if ' ' in inp:                 
    inp = re.sub(r' ','+',inp)

# Search word on site and get results.
response = requests.get('https://www.namasha.com/search?q= %s' %inp)        
soup = BeautifulSoup(response.text,'html.parser')  

# Print the titles and urls of video
for link in soup.findAll('a',attrs={'class':'thumbnail-title thumbnail-url flex-shrink-1 stretched-link'}):
    print(link.text)
    print(link.get('href'))
