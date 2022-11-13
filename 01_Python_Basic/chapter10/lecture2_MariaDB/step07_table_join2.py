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
    
    # outer join
    dname = input('join 부서명 입력 : ')
    sql =f"""select e.eno, e.ename, e.pay, d.dname
    from emp e right outer join dept d
    on e.dname = d.dname and d.dname = '{dname}'"""
    
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data :
        # 3개 레코드 출력 
        #print(row[0], row[1], row[2], row[3])
        
        # 정상 레코드 출력 
        if row[0] and row[1] and row[2] and row[3] :
            print(row[0], row[1], row[2], row[3])            

    print('검색된 레코드 수 :', len(data))
    
    # subquery1 : 부서번호(dept) -> 사원정보(emp) 출력
    dno = int(input('부서번호 입력 : ')) 
    sql=f"""select eno, ename, hiredate, dname from emp 
     where dname = (select dname from dept where dno = {dno}) """
                 
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data :
        print(row[0], row[1], row[2], row[3])
        
    print('검색된 레코드 수 :', len(data))
    
    # subquery2 : 사원이름(emp) -> 부서정보(dept) 출력 
    name = input('사원 이름 입력 : ')
    sql =f"""select  * from dept where dname = 
    (select dname from emp where ename = '{name}')"""
    
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data :
        print(row[0], row[1], row[2])
        
    print('검색된 레코드 수 :', len(data))
        
        
except Exception as e :
    print('db error :', e)
finally:
    cursor.close()
    conn.close()    




