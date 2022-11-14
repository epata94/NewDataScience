import csv
import MySQLdb
from datetime import datetime, date

con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='open_source', passwd='1111')
c = con.cursor()

c.execute("""INSERT INTO Suppliers2 () VALUES (%s, %s, %s, %s, %s);""", data)
con.commit()

# Query the Suppliers table
c.execute("SELECT * FROM Suppliers2")
rows = c.fetchall()
for row in rows:
	row_list_output = []
	for column_index in range(len(row)):
		row_list_output.append(str(row[column_index]))
	print(row_list_output)
