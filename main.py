from bs4 import BeautifulSoup
import categories
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
count = 0

# LOOP OVER EACH CATEGORY
for category_link in categories.list_all_categories:

    plc_holder_link = category_link.format('', None)
    plc_response = requests.get(plc_holder_link, verify=False, allow_redirects=False)
    soup = BeautifulSoup(plc_response.content, 'html.parser')
    
    while plc_response.status_code == 200:
        plc_holder_link = category_link.format(count)
        plc_response = requests.get(plc_holder_link, verify=False, allow_redirects=False)
        
        if plc_response.status_code != 200:
            if count < 1:
                print(f'Status code: {plc_response.status_code} --> {category_link}'.format('', count))
            else:
                print(f'Status code: {plc_response.status_code} --> {category_link}'.format('s-', count))
                break
        
        print(f'Status code: {plc_response.status_code} --> {category_link}'.format(count))
        count += 1
    
    count = 1
        
    # for item in categories.list_all_categories:
        # print(f'{item}'.format(count))
    # if 'https://www.business.bg/o' in 
    # LOOP OVER EACH LINK IN EACH CATEGORY
    # for link in soup.find_all('a'):
    #     f = open("./links.txt", "a")
    #     f.write(link.get('href'))
    #     f.write('\n')
    #     f.close()
    #     print(link.get('href'))
