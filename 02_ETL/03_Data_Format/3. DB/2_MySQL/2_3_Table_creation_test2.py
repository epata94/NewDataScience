import mysql.connector
create_table_sql = '''
create table test(
supplier_name varchar(20)
);
'''
mydb = mysql.connector.connect(host='localhost',user='open_source', passwd='1111', db='my_suppliers')
my_cursor = mydb.cursor()
my_cursor.execute(create_table_sql)

# 생성이 되어 있는 상태에서 같은 테이블을 생성하려고 한다면 아래와 같이 에러 발생
# mysql.connector.errors.ProgrammingError: 1050 (42S01): Table 'test' already exists