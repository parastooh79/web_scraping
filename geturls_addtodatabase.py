# In this program, we read the names of the videos and their links from the site and add them into the database. 
# Our database is MongoDB.




from typing import Text
import pymongo
import requests
from bs4 import BeautifulSoup
import re

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["namasha"]
mycollection= mydb["videos"]

result = requests.get('https://www.namasha.com/')
soup = BeautifulSoup(result.text,'html.parser')


for val in soup.find_all('a',attrs={'class':'flex-shrink-0 font-size-sm mr-auto px-0'}):
    print(val.get('aria-label'))
    url = val.get('href')
    response = requests.get(url)
    soup2 = BeautifulSoup(response.text,'html.parser')
    
    for link in soup2.find_all('a',attrs={'class','thumbnail-title thumbnail-url flex-shrink-1 stretched-link'}):
        t = link.text
        t = re.sub(r'\.',' ',t)
        l = link.get('href')
        find_output = mycollection.find_one({str(t):str(l)})
        
        if find_output == None:
            insert_new = mycollection.insert_one({str(t):str(l)})
            print('New video added!')

        else:
            print('This video is in the database')
