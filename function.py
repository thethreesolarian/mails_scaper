import mysql.connector
import params
import requests

# CHECK FOR HTTP STATUS (200, 301 etc)
def request_status(category_link): 
    response = requests.get(category_link, timeout=2, verify=False, allow_redirects=False)
    return response

# PREPARE URLs. IF INITIAL LINK = JUST REMOVES '*/'. 
# IF ANY FURTHER CATEGORY LINK = REPLACE IT WITH THE CURRENT s_count
def links(category):
    if params.s_count < 1:
        category_link = category.replace('*/', '')
    else:
        category_link = category.replace('*/', f's-{params.s_count}/')
    
    return category_link