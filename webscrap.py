import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.geeksforgeeks.org/data-structures/"
headers = {'User-Agent': "Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.
r = requests.get(url=URL, headers=headers)
# print(r.content)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
# print(soup.prettify())

quotes=[]  # a list to store quotes
  
table = soup.find('ul', attrs = {'class':'content-wrapper content-wrapper_links'})
  
for row in table.findAll('li'):
    quote = {}
    quote['Msg'] = row.a.text
    quote['url'] = row.a['href']
    quotes.append(quote)
  
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Msg','url'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)