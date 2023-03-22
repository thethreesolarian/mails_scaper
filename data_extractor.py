from beautifultable import BeautifulTable
from bs4 import BeautifulSoup
import categories
import re
import requests
import urllib3

# Write the result to a log txt file
def write_links_to_file():
    links_file = open("./structured.txt", "a")
    links_file.write(f'{table}')
    links_file.close()
    
def write_data_into_table():
    links_file = open("./structured.txt", "a")
    links_file.write(f'{table}')
    # links_file.write('\n')
    links_file.close()

# Handling SSL and verification errors
###################################
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = categories.list_all_categories[0].replace('/*/', '/')
response = requests.get(url, verify=False)
###################################

s_count = 0

# Creating a table to hold the data
###################################
table = BeautifulTable()
table.columns.header = (["Company name", "Company e-mail", "Company phone", "Company describtion"])
table.columns.width = 30
###################################

for category in categories.list_all_categories:
    
    temp_link = category
    category = category.replace('*/', '')
    link = category
    print(link)
    
    while response.status_code == 200:
        if s_count > 0:
            category = temp_link
            category = category.replace('*/', f's-{s_count}/')    
            response = requests.get(category, verify=False, allow_redirects=False)
            link = category
        # Get the content of the web page as a string
        response = requests.get(link, verify=False, allow_redirects=False)
        text = BeautifulSoup(response.content, 'html.parser')
        text = str(response.text)
        
        # Goes over each company on the web page and collect:
        for title in re.finditer('<meta itemprop="name" content="', text):
            try:
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
                describtion_end -= 30

                # Create variables to hole the above data
                company_name = text[title_start:title_end]
                company_mail = text[mail_start:mail_end].replace('\t', '')
                company_phone = text[phone_start:phone_end]
                
                company_describtion = text[describtion_start:describtion_end].replace('\t', '')
                company_describtion = company_describtion.replace('\r', '')
                
                # Insert it into the table
                table.rows.append([company_name, company_mail, company_phone, company_describtion])
                print(company_name)
            except:
                print(f'Error occured {company_name}')
        # print(table)
        
        if s_count < 1:
            write_data_into_table()
            
        s_count += 1