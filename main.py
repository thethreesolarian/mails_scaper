from bs4 import BeautifulSoup
import categories
import requests
from urllib.request import urlopen
 
# VARIABLES 
base_url = 'https://bgfirms.info/%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F/'
reqs = requests.get(base_url)
soup = BeautifulSoup(reqs.text, 'html.parser')
count = 0
category = categories.list_all_categories

# LOOP OVER ALL URLS 
urls = []

for link in category:
    url = f'{base_url}{category[count]}'
    count += 1

    for link in soup.find_all('a'):
        page = link.get('href')
        # print("https://bgfirms.info", end='')
        
        next_page = urlopen(url)
        html_bytes = next_page.read()
        html = html_bytes.decode("utf-8")

        print(html)
        
