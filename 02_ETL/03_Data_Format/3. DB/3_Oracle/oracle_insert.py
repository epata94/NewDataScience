import cx_Oracle

conn = cx_Oracle.connect('student/1111@localhost:1521/xe')
# For example, if your user name contains ‘\’, you’ll need to place ‘r’ before the user name: user=r’User Name’
cur = conn.cursor()
print("OK")
f = open("4. New Companies/company.txt", 'r')
lines = f.readlines()

# cur.execute("""insert into company(company_code,founder) VALUES('C93','Jesse')""") # SQL에 ;를 붙이면 에러난다.
for line in lines:
    elements = line.split()
    company_code = elements[0]
    founder = elements[1]
    expected_sql = "insert into company(company_code,founder) VALUES('"+company_code+"','"+founder+"')"
    # sql_transaction = 'insert into company(company_code,founder) VALUES(\''+company_code+'\',\''+founder+'\');'

    print(f'Procession.. [{expected_sql}]')
    # cur.execute("insert into company(company_code,founder) VALUES(?,?);",elements)
    cur.execute(expected_sql)


conn.commit()
cur.close()
conn.close()

# for company_info in c:
#     print(company_info[0]+' '+company_info[1])