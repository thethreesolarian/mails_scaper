from bs4 import BeautifulSoup
import categories
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
count = 0

def write_links_to_file():
    links_file = open("./links.txt", "a")
    links_file.write(category_link)
    links_file.write('\n')
    links_file.close()


# LOOP OVER EACH CATEGORY
for category_link in categories.list_all_categories:

    if count < 1:
        
        temp_link = category_link
        category_link = category_link.replace('*/', '')
        print(category_link)
        write_links_to_file()
        
        response = requests.get(category_link, verify=False, allow_redirects=True)
        soup = BeautifulSoup(response.content, 'html.parser')
        count += 1

        while response.status_code == 200:
            category_link = temp_link
            category_link = category_link.replace('*/', f's-{count}/')
            response = requests.get(category_link, verify=False, allow_redirects=False)
            
            write_links_to_file()
            print(category_link)
            count += 1
            
    # if count > 0:
    #     category_link = category_link.replace('*/', f's-{count}/')
    
    count = 0

