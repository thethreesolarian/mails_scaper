from bs4 import BeautifulSoup
import categories
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
count = 0

def write_links_to_file():
    links_file = open("./links.txt", "a")
    links_file.write(f'{category_link}\n')
    # links_file.write('\n')
    links_file.close()

# LOOP OVER EACH CATEGORY
for category_link in categories.list_all_categories:

    if count < 1:
        
        temp_link = category_link
        category_link = category_link.replace('*/', '')
        print(category_link)
        # write_links_to_file()
        
        response = requests.get(category_link, verify=False, allow_redirects=False)
        soup = BeautifulSoup(response.content, 'html.parser')
        title_end_index = soup.text
        title_end_index = title_end_index.index(' |')
        # print(title_end_index)
        print(soup.text[6:title_end_index])

        while response.status_code == 200:
            count += 1
            category_link = temp_link
            category_link = category_link.replace('*/', f's-{count}/')
            response = requests.get(category_link, verify=False, allow_redirects=False)
            
            if response.status_code == 200:
                # write_links_to_file()
                print(soup.content)
                print(category_link)
    
    count = 0