import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='open_source', passwd='1111', db='my_suppliers')
my_cursor = mydb.cursor()
create_table_sql = '''
CREATE TABLE IF NOT EXISTS Suppliers (
			 Supplier_Name VARCHAR(20),
             Invoice_Number VARCHAR(20),
             Part_Number VARCHAR(20),
             Cost FLOAT,
			 Purchase_Date DATE);
'''
my_cursor.execute(create_table_sql)

# mysql> show tables;
# +------------------------+
# | Tables_in_my_suppliers |
# +------------------------+
# | suppliers              |
# | test                   |
# +------------------------+
# 2 rows in set (0.00 sec)