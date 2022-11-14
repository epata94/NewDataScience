# py -m pip install mysqlclient
import csv
import MySQLdb
import sys
from datetime import datetime, date

# Path to and name of a CSV input file
input_file = sys.argv[1] # supplier_data.csv

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
			# str(row[column_index]), '%m/%d/%Y')) # 대문자 Y로 저장하면 에러남남			# %Y: year is 2016; %y: year is 15
			a_date = a_date.strftime('%y-%m-%d')
			# a_date = a_date.strftime('%Y-%m-%d')
			data.append(a_date)
	print(data)
	# c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)
	# 아래 코드는 SQL injection 공격에 취약하다.
	# c.execute("""INSERT INTO Suppliers VALUES %r;"""%(tuple(data),))

	# var_string =   ', '.join('?' * len(data)) # excutemany 일경우에
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
