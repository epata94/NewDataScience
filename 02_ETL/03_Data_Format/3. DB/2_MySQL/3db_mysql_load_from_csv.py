# py -m pip install mysqlclient
import csv
import MySQLdb
import sys
from datetime import datetime, date

# Path to and name of a CSV input file
input_file = 'supplier_data.csv'

# Connect to a MySQL database
#con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='python_training', passwd='python_training')
# con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', passwd='1111')
#localhost: 현재 자신의 컴퓨터(127.0.0.1)
# port: 3306 <= MySQL 설치시 Default port번호
# db: Database명 create database my_suppliers <= 이렇게 생성한 db명과 매칭
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='open_source', passwd='1111')
c = con.cursor()

# Read the CSV file
# Insert the data into the Suppliers table
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		if column_index < 4:
			data.append(str(row[column_index]).lstrip('$')\
			.replace(',', '').strip())
		else:
			a_date = datetime.date(datetime.strptime(\
			str(row[column_index]), '%m/%d/%y'))
			# MYSQL의 날자 타입에 맞게 'YYYY-MM-DD' 형식으로 변경
			a_date = a_date.strftime('%y-%m-%d')
			data.append(a_date)
	print(data)
	# c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)

	var_string =   ', '.join('?' * len(data)).replace('?','%s')
	query_string = "INSERT INTO Suppliers VALUES (%s);"%var_string
	c.execute(query_string, data)

con.commit()

# Query the Suppliers table
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
	row_list_output = []
	for column_index in range(len(row)):
		row_list_output.append(str(row[column_index]))
	print(row_list_output)
