import sqlite3
import csv
import MySQLdb
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', \
user='open_source', passwd='1111')
c = con.cursor()
# delete from [테이블명] where [필드명]=[필터링조건값]
# 특정 레코드(행)을 삭제하는 SQL 명령어
delete_table = """
delete 
from Suppliers
where Supplier_Name='Supplier Z'                    
"""
c.execute(delete_table)
con.commit()

c.execute("SELECT * FROM Suppliers")

rows = c.fetchall()
for row in rows:
	row_list_output = []
	for column_index in range(len(row)):
		row_list_output.append(str(row[column_index]))
	print(row_list_output)