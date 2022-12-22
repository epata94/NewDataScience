# pip install --upgrade pip
import cx_Oracle
import pandas as pd

conn = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
cur = conn.cursor()
print("OK")
cur.execute('select * from museum')

for record in cur:
    print(record)


