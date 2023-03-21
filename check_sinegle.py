from bs4 import BeautifulSoup
import categories
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
count = 0

def write_links_to_file():
    links_file = open("./single_page.txt", "a")
    links_file.write(f'{category_link}\n')
    # links_file.write('\n')
    links_file.close()

# LOOP OVER EACH CATEGORY
general_count = 0
categories_count = len(categories.list_all_categories)
for category_link in categories.list_all_categories:

    if count < 1:
        
        temp_link = category_link
        category_link = category_link.replace('*/', '')
        # print(category_link)
        # write_links_to_file()
        # print(f'Progress: {int(general_count/578 * 100)}% ', end='\r')
        general_count += 1
        progress = int(general_count/categories_count * 100)
        
        response = requests.get(category_link, timeout=10, verify=False, allow_redirects=False)
        soup = BeautifulSoup(response.content, 'html.parser')
        # count += 1

        while response.status_code == 200:
            try:
                print(f'[Progress: {progress}%], Count: {count}, URLs left: {categories_count - general_count}, URL: {category_link}', end='\r')
                
                # print(f'|               Count : {count}', end='\r')
                count += 1
                category_link = temp_link
                category_link = category_link.replace('*/', f's-{count}/')
                response = requests.get(category_link, timeout=1, verify=False, allow_redirects=False)
                
                if count == 400:
                    # write_links_to_file()
                    # print(category_link)
                    write_links_to_file()
                    break
            except:
                print(f'Error URL: {category_link}')
    
    count = 0