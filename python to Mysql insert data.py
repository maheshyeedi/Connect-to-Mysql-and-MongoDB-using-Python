#connect to MySQL DB and inserting records into predefined Employees table
import mysql.connector
#
cnx= mysql.connector.connect(user='root',password='password',database='pythondb',host='localhost')

#SQL query into cursor
cursor = cnx.cursor()

query=("INSERT INTO employees(personid,lastname,firstname,city,department,gender)""VALUES(%s, %s, %s, %s, %s, %s)")
data_emp =('2017','python','mongodb','bangalore','dev','male')

#insert new employee record
cursor.execute(query,data_emp)

#Data is commited to Database
cnx.commit()

for (lastname,firstname) in cursor:
	print("{0},{1} were working in {2}".format(lastname,firstname,department))

#close connection
cursor.close()
cnx.close()