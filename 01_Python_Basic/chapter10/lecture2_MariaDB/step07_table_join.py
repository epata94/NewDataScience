'''
Created on 2019. 4. 29.

@author: 702-2-04
'''
import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    
    # inner join
    pay = int(input('join 급여 입력 : '))
    sql =f"""select e.eno, e.ename, e.pay, d.dname, daddr
    from emp e inner join dept d
    on e.dname = d.dname and e.pay >= {pay}"""
    
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data :
        print(row[0], row[1], row[2], row[3], row[4])

    print('검색된 레코드 수 :', len(data))

        
except Exception as e :
    print('db error :', e)
finally:
    cursor.close()
    conn.close()    




