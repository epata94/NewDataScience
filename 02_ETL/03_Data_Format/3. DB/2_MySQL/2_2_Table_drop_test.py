import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='open_source', passwd='1111', db='my_suppliers')
my_cursor = mydb.cursor()
drop_table_sql = '''
    drop table test
'''
my_cursor.execute(drop_table_sql)
# mysql> show tables;
# Empty set (0.00 sec)