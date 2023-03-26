# import the modules
from pymysql import*
import xlwt
import pandas.io.sql as sql

# connect the mysql with the python
con=connect(user="data_any",password="data_123!@#",host="localhost",database="mails", port=41063)

# read the data
df=sql.read_sql('select * from data',con)

# print the data
print(df)

# export the data into the excel sheet
df.to_excel('data.xls')

