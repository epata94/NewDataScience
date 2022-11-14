import sqlite3

# Create an in-memory SQLite3 database
# Create a table called sales with four attributes
con = sqlite3.connect(':memory:')


# Query the sales table
# :memory: 는 휘발성(volatile)이기 때문에 프로그램이 종료가 된 후에는
# 그 이전에 작업한 모든 내역은 사라진다.
# 따라서 아래 select문은 정상 수행되지 않는다.
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

# Count the number of rows in the output
row_counter = 0
for row in rows:
	print(row)
	row_counter += 1
print('Number of rows: {}'.format(row_counter))
