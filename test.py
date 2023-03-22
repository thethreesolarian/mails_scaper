from beautifultable import BeautifulTable
import requests
import urllib3
import re

# Write the result to a log txt file
def write_links_to_file():
    links_file = open("./structured.txt", "a")
    links_file.write(f'{table}')
    # links_file.write('\n')
    links_file.close()

# Creating a table to hold the data
table = BeautifulTable()
table.columns.header = (["Company name", "Company e-mail", "Company phone", "Company describtion"])
table.columns.width = 30

# Handling SSL and verification errors
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
response = requests.get('https://www.business.bg/o-9/stroitelstvo.html', verify=False)

# Get the content of the web page as a string
text = str(response.text)

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