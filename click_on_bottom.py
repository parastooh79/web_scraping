# There are many links about different topics in home page of namasha site 
# Here we click on bottom to show all videos and get titles and urls of videos in new page 

import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.namasha.com/')
soup = BeautifulSoup(result.text,'html.parser')

for val in soup.find_all('a',attrs={'class':'flex-shrink-0 font-size-sm mr-auto px-0'}):
    print(val.get('aria-label'))               # Print the title of topic
    url = val.get('href')                      # Find url of topic
    response = requests.get(url)               # Send Request to site and gete data
    soup2 = BeautifulSoup(response.text,'html.parser')
    
    for link in soup2.find_all('a',attrs={'class','thumbnail-title thumbnail-url flex-shrink-1 stretched-link'}):
        print(link.text)                # Print the name of video 
        print(link.get('href'))         # Print the url of video

    print('-----------------------------------------------------------------------------------------')
