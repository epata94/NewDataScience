import mysql.connector
# IF NOT EXISTS로 생성시 에러를 피할 수 있다.
create_table_sql = '''
create table IF NOT EXISTS test(
supplier_name varchar(20)
);
'''
mydb = mysql.connector.connect(host='localhost',user='open_source', passwd='1111', db='my_suppliers')
my_cursor = mydb.cursor()
my_cursor.execute(create_table_sql)
