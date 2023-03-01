from bs4 import BeautifulSoup
import categories
import requests
from urllib.request import urlopen
 
# VARIABLES 
url = '' # 'https://bgfirms.info/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
count = 0
category = categories.list_all_categories

# LOOP OVER ALL URLS 
urls = []

for link in category:
    url = category[link]


# for link in soup.find_all('a'):
#     page = link.get('href')
#     print("https://bgfirms.info", end='')
    
#     next_page = urlopen(url)
#     html_bytes = next_page.read()
#     html = html_bytes.decode("utf-8")

#     print(html)
    
