from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# specify the URL of the page to scrape
url = 'https://www.business.bg/'

# send a request to the website and get the HTML content
response = requests.get(url, verify=False)

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# loop through each link in the page and print its href attribute
for link in soup.find_all('a'):
    current_url = link.get('href')
    if current_url != 'https://www.business.bg' and current_url != '#' and current_url != '#/':
        f = open("./links.txt", "a")
        f.write(link.get('href'))
        f.write('\n')
        f.close()
        print(link.get('href'))
