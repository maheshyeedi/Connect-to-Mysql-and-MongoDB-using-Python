# Connect to MySQL and retrieving data insert

import mysql
import mysql.connector

#creating a connection
cnx= mysql.connector.connect(user='root',password='password',database='pythondb',host='localhost')


cursor = cnx.cursor()

query=("SELECT lastname,firstname,department ""FROM employees")

#SQL query execution
cursor.execute(query)
print (cursor.fetchall())  # 2nd method to print the values

#Data is commited to Database
cnx.commit()

for (lastname,firstname,department) in cursor:
	print("{0} {1} were working in {2}".format(lastname,firstname,department))

#close connection
cursor.close()
cnx.close()