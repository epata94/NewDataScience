import cx_Oracle

conn = cx_Oracle.connect('student/1111@localhost:1521/xe')
# For example, if your user name contains ‘\’, you’ll need to place ‘r’ before the user name: user=r’User Name’
cur = conn.cursor()
print("OK")
f = open("lead_manager.txt", 'r')
lines = f.readlines()
rows=[]
for line in lines:
    elements = line.split()
    rows.append(elements)

cur.executemany("insert into Lead_Manager(lead_manager_code, company_code) VALUES(:1,:2)", rows)


conn.commit()
cur.close()
conn.close()

# for company_info in c:
#     print(company_info[0]+' '+company_info[1])