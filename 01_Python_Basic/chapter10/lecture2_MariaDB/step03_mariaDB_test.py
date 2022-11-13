'''
0. mariaDB 설치 : 설치, DB/TABLE/USER 생성
1. PyMySql 설치 : Files > Settings
2. pymysql 패키지 확인 : import pymysql

'''

import pymysql
print(pymysql.version_info) # (1, 3, 12, 'final', 0)

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try :
    # db 연동 객체 
    conn = pymysql.connect(**config)
    # sql문 실행 객체
    cursor = conn.cursor()

    sql = "show tables"
    cursor.execute(sql)
    
    tables = cursor.fetchall()
    # 전체 table 목록 출력
    print(tables)

    # table 유무
    if tables:
        print('table 있음')
    else:
        print('table 없음')

except Exception as e :
    print('db error :', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()


