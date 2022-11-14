import cx_Oracle

conn = cx_Oracle.connect('student/1111@localhost:1521/xe')
# For example, if your user name contains ‘\’, you’ll need to place ‘r’ before the user name: user=r’User Name’
cur = conn.cursor()
print("OK")

table_source_list = ['hackers.txt','Challenges.txt']

index = 1
for table_source in table_source_list:
    f = open(table_source,'r')
    lines = f.readlines()
    rows=[]
    for line in lines:
        elements = line.split()
        rows.append(elements)
    if index == 1:
        cur.executemany("insert into Hackers11(hacker_id, name) VALUES(:1,:2)", rows)
    elif index == 2:
        cur.executemany("insert into Challenges11(challenge_id, hacker_id) VALUES(:1,:2)", rows)

    print(f'{table_source} is completed!')
    index += 1


conn.commit()
cur.close()
conn.close()

# for company_info in c:
#     print(company_info[0]+' '+company_info[1])