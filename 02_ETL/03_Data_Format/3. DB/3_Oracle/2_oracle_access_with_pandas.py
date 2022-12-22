# pip install --upgrade pip
import cx_Oracle
import pandas as pd

conn = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
cur = conn.cursor()
cur.execute("""
SELECT column_name from cols
where table_name = 'MUSEUM'
""")


# for record in cur:
#     print(record)

column_list = [record[0] for record in cur]
print(column_list)

cur.execute('select * from museum')
df = pd.DataFrame(cur, columns=column_list)
print(df.head())

cur.execute("""
SELECT 시설명, 박물관미술관구분,청소년관람료
from museum
where 청소년관람료 > 1500
""")


print("Selection and Projection Query")
df = pd.DataFrame(cur, columns=['시설명', '박물관미술관구분','청소년관람료'])
print(df.head())