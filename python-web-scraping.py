import requests
from bs4 import BeautifulSoup

url="http://books.toscrape.com/"
data=requests.get(url)

#print(r.content)

#to get data
soup=BeautifulSoup(data.content)

#to print data
print(soup)

#to convert data into a structured one
print(soup.prettify())

#to find all anchor tags
print(soup.find_all("a"))

