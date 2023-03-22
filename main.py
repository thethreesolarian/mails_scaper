from beautifultable import BeautifulTable
from bs4 import BeautifulSoup
import categories
import re
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def write_links_to_file(link):
    links_file = open("./links.txt", "a")
    links_file.write(f'{link}\n')
    # links_file.write('\n')
    links_file.close()

def get_data():
    
    # Handling SSL and verification errors
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get(main_func(category_link), verify=False)
    
    # Get the content of the web page as a string
    text = str(response.text)

    # Creating a table to hold the data
    table = BeautifulTable()
    table.columns.header = (["Company name", "Company e-mail", "Company phone", "Company describtion"])
    table.columns.width = 30

    # Goes over each company on the web page and collect:
    for title in re.finditer('<meta itemprop="name" content="', text):

        # The tile of the firm
        title_start = title.end()
        title_end = text.find('"', title_start)
        
        # It's e-mail
        mail_start = text.find('email"', title_end)
        mail_start += 16
        mail_end = text.find('"', mail_start)
        
        # It's phone number
        phone_start= text.find('telephone"', mail_end)
        phone_start += 20
        phone_end = text.find('"', phone_start)
        
        # And the describtion if it exists
        describtion_start = text.find('firm_text', phone_end)
        describtion_start += 11
        describtion_end = text.find('<', describtion_start)
        describtion_end -= 20
        
        # Create variables to hole the above data
        company_name = text[title_start:title_end]
        company_mail = text[mail_start:mail_end]
        company_phone = text[phone_start:phone_end]
        company_describtion = text[describtion_start:describtion_end]
        
        # Insert it into the table
        table.rows.append([company_name, company_mail, company_phone, company_describtion])
    # print(table)
    write_links_to_file()
    # return link

s_count = 0

# LOOP OVER EACH CATEGORY FRON FILE categories.py
for category_link in categories.list_all_categories:
    def main_func(link):        
        # FOR THE FIRST LINK FOR EACH CATEGORY
        if s_count < 1:
            
            temp_link = category_link
            category_link = category_link.replace('*/', '')
            link = category_link
            print(link)
            
            response = requests.get(category_link, verify=False, allow_redirects=False)
            text = BeautifulSoup(response.content, 'html.parser')
            
            get_data(link=category_link)

            while response.status_code == 200:
                s_count += 1
                category_link = temp_link
                category_link = category_link.replace('*/', f's-{s_count}/')
                response = requests.get(category_link, verify=False, allow_redirects=False)
                link = category_link
                
                if response.status_code == 200:
                    # write_links_to_file()
                    print(text.content)
                    print(category_link)
        
        s_count = 0
        return link
    get_data()
        
# main_function()
# get_data(link='kkkkkk')