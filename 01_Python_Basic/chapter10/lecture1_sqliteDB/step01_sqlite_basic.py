'''
sqlite3 - 내장형 DBMS
  - 기기 내부에서만 사용 
  - 외부 접근 허용 안됨 
'''

import sqlite3

print(sqlite3.sqlite_version_info) # (3, 21, 0)

try :
    # db 연동 객체 
    conn = sqlite3.connect("chapter10/data/sqlite_db") # db 생성 -> 연결 object
    # sql 실행 객체 
    cursor = conn.cursor()
    
    # table 생성
    sql= 'create table if not exists test_table(name text(10), phone text(15), addr text(50))'
    cursor.execute(sql)
    
    # 레코드 추가 
    cursor.execute("insert into test_table values('홍길동', '010-1111-1111', '서울시')")
    cursor.execute("insert into test_table values('이순신', '010-2222-2222', '해남시')")
    cursor.execute("insert into test_table values('강감찬', '010-1111-1111', '평양시')")
    conn.commit() # db 반영 
    
    # 레코드 조회
    cursor.execute("select * from test_table")
    rows = cursor.fetchall()
    
    for row in rows :
        print(row)
    
    print('이름 \t전화번호 \t\t주소')
    for row in rows :
        print(row[0],'\t',row[1],'\t',row[2]) 
    
except Exception as e :
    print('db 연동 실패 : ', e)
    conn.rollback() # 실행 취소 
    
finally:
    # object.close()
    cursor.close()
    conn.close()
    
    





