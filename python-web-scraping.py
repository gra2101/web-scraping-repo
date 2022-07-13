from pyclbr import Class
import requests
from bs4 import BeautifulSoup

url="http://books.toscrape.com/"
data=requests.get(url)

soup=BeautifulSoup(data.content, "html.parser")
soup.prettify()
soup.find_all('div')
listdata= soup.find('ul', {'class':'nav nav-list'})
# for li in listdata:
#     print(li.get_text())
print(listdata.find_all())



#to get data
# soup=BeautifulSoup(data.content)

# #to print data
# print(soup)

# #to convert data into a structured one
# print(soup.prettify())

# #to find all anchor tags
# print(soup.find_all("a"))
# # for link in soup.find_all("a"):
# #     print(link.text)

# soup.find_all("li")
# for text in soup.find_all("li"):
#     print(text)
