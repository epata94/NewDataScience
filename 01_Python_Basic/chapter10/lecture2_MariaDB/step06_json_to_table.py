'''
json -> db table
  1. json file read
  2. DataFrame 생성
  3. table 생성/레코드 추가(json data)
  4. table에 레코드 조회

json file decoding
  - json file(json 문자열) -> python dict
  1. {key:value, key:value} -> row : usagov_bitly.txt
      json.loads()
  2. [{row1}, {row2}, {rown}] -> list[{}] : labels.json
      json.load()
'''
import json

# 1. json file decoding
file = open("chapter10/data/labels.json", mode='r', encoding="utf-8")
#lines = file.read()
#print(lines)
# decoding : json 문자열 -> dict
lines = json.load(file)
print(type(lines)) # <class 'list'>
print(len(lines)) # 30
print(type(lines[0])) # <class 'dict'>

# row 단위 출력
cnt = 0
for line in lines :
    cnt += 1
    print(cnt, '->', line)

# 2. DataFrame 생성
import pandas as pd
df = pd.DataFrame(lines)
print(df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30 entries, 0 to 29
Data columns (total 5 columns):
id         30 non-null int64 -> int
url        30 non-null object -> varchar()
name       30 non-null object -> varchar()
color      30 non-null object -> varchar()
default    30 non-null bool -> str -> varchar()
'''
print(df.head())

# 3. db table 생성 -> 레코드 추가
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

    # table 생성
    '''
    sql = """create table labels(
    id int not null, 
    url varchar(150) not null,
    name varchar(50) not null,
    color varchar(50) not null,
    de char(5) 
    )"""
    cursor.execute(sql) # table 생성
    '''

    # 레코드 조회
    cursor.execute("select * from labels")
    rows = cursor.fetchall()
    if rows :
        print("labels 레코드 조회")
        for row in rows :
            print(row)

        print("전체 레코드 수 :", len(rows))
    else :
        print("labels 레코드 삽입")
        for i in range(30) :
            uid = df.id[i] # df['column'] or df.column
            url = df.url[i]
            name = df.name[i]
            color = df.color[i]
            de = str(df.default[i]) # bool -> str
            sql = f"insert into labels values({uid},'{url}','{name}','{color}','{de}')"
            cursor.execute(sql)
            conn.commit() # db 반영
except Exception as e:
    print("db error : ", e)
finally:
    cursor.close()
    conn.close()