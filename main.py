from bs4 import BeautifulSoup
import categories
import requests
from urllib.request import urlopen
import urllib.parse

# VARIABLES
base_url = 'https://bgfirms.info/категория/'
reqs = requests.get(base_url)
soup = BeautifulSoup(reqs.text, 'html.parser')
count = 0
category = categories.list_all_categories

# LOOP OVER ALL URLS
urls = []

for link in category:
    url = f'{base_url}{category[count]}'
    count += 1

    for inner_link in soup.find_all('a'):
        page = inner_link.get('href')
        if  page != '#' or  page != '/за-нас':
        
            
            # print("https://bgfirms.info", end='')

            # url_encoded = urllib.parse.quote(url, safe='')
            # next_page = urlopen(url_encoded)
            # html_bytes = next_page.read()
            # html = html_bytes.decode("utf-8", errors="ignore")

            print(page)
