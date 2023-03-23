# data = mysql.connector.connect(
#   host="localhost",
#   user="data_any",
#   password="data_123!@#",
#   database="mails",
#   port = "41063"
# )

# cursor = data.cursor()

import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="data_any",
        password="data_123!@#",
        database="mails",
        port = "41063"
        )

    mySql_insert_query = "SELECT company_name FROM data WHERE EXISTS(SELECT * FROM Sales WHERE tax>150)"


    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")