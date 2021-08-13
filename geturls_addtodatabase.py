# In this program, we read the names of the videos and their links from the site and add them into the database. 
# Our database is MongoDB.

# Step 1 : import libraries
from typing import Text
import pymongo
import requests
from bs4 import BeautifulSoup
import re

# Step 2 : connecting to database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["namasha"]                   # My database name
mycollection= mydb["videos"]                 # My collection name


# Step 3 : Send a request and read all the site 
result = requests.get('https://www.namasha.com/')
soup = BeautifulSoup(result.text,'html.parser')

# Step 4 : Find the button link and submit a new request. ( Click on the buttons )
for val in soup.find_all('a',attrs={'class':'flex-shrink-0 font-size-sm mr-auto px-0'}):
    print(val.get('aria-label'))
    url = val.get('href')
    response = requests.get(url)
    soup2 = BeautifulSoup(response.text,'html.parser')
    
    # Step 5 : Find titles and video links
    for link in soup2.find_all('a',attrs={'class','thumbnail-title thumbnail-url flex-shrink-1 stretched-link'}):
        t = link.text
        t = re.sub(r'\.',' ',t)
        l = link.get('href')
        
        # Step 6 : Check the database for duplicate videos and save if not duplicate
        find_output = mycollection.find_one({str(t):str(l)})
        
        if find_output == None:
            insert_new = mycollection.insert_one({str(t):str(l)})
            print('New video added!')

        else:
            print('This video is in the database')
