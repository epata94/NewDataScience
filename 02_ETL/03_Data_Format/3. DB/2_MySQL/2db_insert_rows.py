# 목적
# 1. 비휘발성 데이터 베이스 생성하기
# 2. 외부데이터로부터 초기 DB table 값 생성
import csv
import sqlite3
import sys

# Path to and name of a CSV input file
# input_file = sys.argv[1] # supplier_data_org.csv
input_file = 'supplier_data.csv'

# Create a table called Suppliers with five attributes
# SQLLite의 경우는 DB명이 파일로 1:1 매칭이 된다.
con = sqlite3.connect('Suppliers.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Suppliers
				(Supplier_Name VARCHAR(20), 
				Invoice_Number VARCHAR(20),
				Part_Number VARCHAR(20),
				Cost FLOAT,
				Purchase_Date DATE);"""
c.execute(create_table)
con.commit()

# Read the CSV file
# Insert the data into the Suppliers table
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None) # header 건너뛰고 data만 접근 하기 위하여
print("CSV 원본 데이터 현황")
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		data.append(row[column_index])
	print(data)
	c.execute("INSERT INTO Suppliers VALUES (?, ?, ?, ?, ?);", data)
con.commit()

# Query the Suppliers table
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
print("\nSuppliers 테이블 레코드값 현황")
for row in rows:
	output = []
	for column_index in range(len(row)):
		output.append(str(row[column_index]))
	print(output)
