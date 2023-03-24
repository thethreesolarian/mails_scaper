from beautifultable import BeautifulTable
from bs4 import BeautifulSoup
import categories
import function
import mysql.connector
import params
import re
import requests
import urllib3


class DataExtractor:
    
    s_count = 0
    line = 0
    

    
    # Handling SSL and verification errors
    ###################################
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = categories.list_all_categories[0].replace('/*/', '/')
    response = requests.get(url, verify=False)
    ###################################
    
    def __init__(self, category_link, line):
        
        # CHECK FOR HTTP STATUS (200, 301 etc)
        def request_status(category_link): 
            response = requests.get(category_link, timeout=2, verify=False, allow_redirects=False)
            return response

        # PREPARE URLs. IF INITIAL LINK = JUST REMOVES '*/'. 
        # IF ANY FURTHER CATEGORY LINK = REPLACE IT WITH THE CURRENT s_count
        def links(category):
            if s_count < 1:
                category_link = category.replace('*/', '')
            else:
                category_link = category.replace('*/', f's-{s_count}/')
            
            return category_link
    
        # Loop over all CATEGORIES URLs
        for category in categories.list_all_categories:
            category_link = links(category)
            request_status(category_link)
            
            self.category_link = category_link
            self.line = line
            
            # Loop over each page for a given category untill face status != 200
            while response.status_code == 200:
                if s_count > 0:
                    category_link = links(category)
                    response = request_status(category_link)
                    
                    # If the given category_link (URL) returns != 200, go to the main loop
                    if response.status_code != 200:
                        break
                
                # Get the content of the web page as a string
                response = request_status(category_link)
                text = BeautifulSoup(response.content, 'html.parser')
                text = str(response.text)

                # Goes over each company on the web page and collect:
                for title in re.finditer('<meta itemprop="name" content="', text):
                    try:
                        # The category
                        category_start = text.find('"og:title" content="')
                        category_start += 20
                        category_end = text.find('"', category_start)

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
                        category_name = text[category_start:category_end]
                        company_name = text[title_start:title_end]
                        company_mail = text[mail_start:mail_end].replace('\t', '')
                        company_phone = text[phone_start:phone_end]
                        
                        company_describtion = text[describtion_start:describtion_end].replace('\t', '')
                        company_describtion = company_describtion.replace('\r', '')
                        
                        line += 1
                    #     # Insert it into MySQL table                
                    #     sql = f'INSERT INTO data(line_number, category_name, company_name, company_mail, company_phone, company_describtion)' \
                    #     f'VALUES ({line}, \'{category_name}\', \'{company_name}\', \'{company_mail}\', \'{company_phone}\', \'{company_describtion}\')'
                    #     sql_execute()
                
                    except:
                        print(f'Error occured {company_name}')
                    #     data.commit()
                    print(f'{category_link} | {category_name} | {company_name}')
                s_count += 1
            s_count = 0
            # print(category_name)
            # print(line)
            print(category_link.capitalize)
