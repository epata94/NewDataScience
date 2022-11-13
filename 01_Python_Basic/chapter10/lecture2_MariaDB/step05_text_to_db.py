'''
<<작업순서>>
1. table 작성 
2. zipcode.txt read(서울) -> table 저장
3. table  저장 -> 검색 
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
    sql = "select * from zipcode_tab"
    
    cursor.execute(sql)
    dataset = cursor.fetchall()
    print('길이 :', len(dataset))
    
    if len(dataset) > 0 : # 레코드 있는 경우(검색)
        dong = input("검색 동 입력 : ")
        sql = f"select * from zipcode_tab where dong like '%{dong}%'"
        cursor.execute(sql)
        dataset = cursor.fetchall()
        
        for row in dataset :
            print(row[0], row[1],row[2], row[3], row[4])
            
        print('검색된 레코드 : ', len(dataset))
        
        gu = input("검색 구 입력 : ")
        sql = f"select * from zipcode_tab where gu like '%{gu}%'"
        cursor.execute(sql)
        dataset = cursor.fetchall()
        
        for row in dataset :
            print(row[0], row[1],row[2], row[3], row[4])
            
        print('검색된 레코드 : ', len(dataset))
        
    else : # 레코드 없는 경우(레코드 추가) 
        file = open("../data/zipcode.txt", mode='r', encoding='utf-8')
        lines = file.readline() 
        while lines :
            line = lines.split(sep='\t') # 칼럼 단위 
            if line[1] == '서울' : # 서울 지역 db 저장
                code = str(line[0]); city=line[1]; gu = line[2]
                dong = line[3]; detail=line[4]                
                if len(detail) > 0 :
                    sql = f"""insert into zipcode_tab 
                    values('{code}','{city}','{gu}','{dong}','{detail}')"""
                else :
                    sql = f"""insert into zipcode_tab(code,city,gu,dong)
                     values('{code}','{city}','{gu}','{dong}')"""
                                    
                cursor.execute(sql) # 저장 
                conn.commit()#  db 반영
                
            lines = file.readline() # 2줄 ~ end
            
        file.close()
        print('~레코드 추가 성공~')
    
except Exception as e:
    print('db error :', e)
finally:
    cursor.close()
    conn.close()









