import sqlite3

con = sqlite3.connect('Suppliers.db')
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

# Query the Suppliers table
con = sqlite3.connect('Suppliers.db')
c = con.cursor()
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
	output = []
	for column_index in range(len(row)):
		output.append(str(row[column_index]))
	print(output)
