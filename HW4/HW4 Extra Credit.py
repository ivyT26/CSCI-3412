#!/usr/bin/env python
# coding: utf-8

# # Name: Ivy Truong
# # Homework 4 Extra Credit

# In[20]:


import urllib.request
from bs4 import BeautifulSoup
import json

#code learned implemented for web scraping: https://www.scrapehero.com/a-beginners-guide-to-web-scraping-part-2-build-a-scraper-for-reddit/

url = "http://www.ucdenver.edu/pages/ucdwelcomepage.aspx"
#read the HTML content of the url
request = urllib.request.Request(url)
htmlDoc = urllib.request.urlopen(request).read()

#pass HTML to Beautiful Soup
soup = BeautifulSoup(htmlDoc, 'html.parser')
#print(soup.prettify()[:]) #used to see the html code of webpage in html format (with all neat spacings)

#finding main table with id docResponsive, this is where all the links should be displayed for the current url
main_table = soup.find("div",attrs = {'id':'docResponsive'})

#getting all the links (or most of them) in the main table 
navLink = main_table.find_all("a", class_ = "navbar-link") #title in text
moreLink = main_table.find_all("a", class_ = "more url") #title apart of title attribute

#extracting title and url of records
data_records = []
for link in navLink:
    title = link.text
    url = link['href']
    
    #prepend http://www.ucdenver.edu to relative urls so it works if it were to be accessed again through the browser
    if not url.startswith('http'):
        url = "http://www.ucdenver.edu" + url
    
    #put record into a dictionary
    record = {
        'title':title,
        'url':url
    }
    data_records.append(record)

for link in moreLink:
    title = link['title']
    url = link['href']
    
    #put record into a dictionary
    record = {
        'title':title,
        'url':url
    }
    data_records.append(record)
print(data_records)

#save data into a JSON file
#creates and opens a file and writes data into the file
with open('data.json', 'w') as outfile:
    json.dump(data_records, outfile)


# In[ ]:




