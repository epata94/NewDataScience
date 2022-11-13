'''
prof table 대상 group 함수 적용
  - bmi table 기준
    label 칼럼 그룹화
    sql =f"""select label, avg(height), avg(weight)
    from bmi_tab group by label
    order by label"""
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
    '''
    gcol = int(input('그룹 칼럼(1. 직급, 2.학과) : '))
    
    gcol = 'position' if gcol == 1 else 'deptno' 
        
    sql =f"""select {gcol}, avg(pay), avg(bonus) 
    from prof group by {gcol} 
    order by {gcol}"""
    '''

    sql = """select label, avg(height), avg(weight)
            from bmi_tab group by label
            order by label"""

    cursor.execute(sql)
    rows = cursor.fetchall()
    print("label\theight\tweight")
    if rows:  # 레코드 검색
        for row in rows:
            print(f"{row[0]}    {row[1]}    {row[2]}")

except Exception as e:
    print('db error :', e)
finally:
    cursor.close()
    conn.close()
'''
label	height	weight
fat    152.3784    70.0811
normal    162.3125    57.4688
thin    175.6129    48.2581
'''