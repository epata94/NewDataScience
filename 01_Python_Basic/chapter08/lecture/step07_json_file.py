'''
JSON 파일[문서]
 - 네트워크상에서 표준으로 사용되는 파일 형식
   
- json 모듈 기능 
 1. encoding : Python 객체(dict or list) -> json 문자열(json file)
 2. decoding : json 문자열 -> Python 객체(dict or list)
'''

import json

# 1. json encoding
'''
 - Python 객체(dict) ->  json 문자열 변경
   형식) json.dumps(object) 
'''
user = { 'id': 1234,  'name': '홍길동'} # Python Dict
print(type(user)) # <class 'dict'>  
print(user['name']) # 홍길동

#  json 인코딩 : dict -> string, ensure_ascii=False -> 한글 사용시 
jsonString = json.dumps(user)#, ensure_ascii=False) # ASCII 인코딩 방식 적용 안함

# 문자열 출력 
print(jsonString) # {"id": 1234, "name": "홍길동"}
print(type(jsonString))   # class str
#print(jsonString['name']) # Error 발생 
print(jsonString[:5]) # {"id"

# 2. json decoding 
'''
 - json 문자열 -> Python 객체(dict or list)
   형식) json.loads(jsonString) 
   에) json 파일(문자열)  -> Python 객체(dict or list)
'''

# json  디코딩
pyObj = json.loads(jsonString)
print(type(pyObj)) # <class 'dict'>
 
# Dict 자료 체크
print(pyObj['name']) # 홍길동
for key in pyObj :
    print(key, ':' , pyObj[key])
    
'''
id : 1234
name : 홍길동
'''    

# 3. json file 읽기
'''
- json 디코딩 : json 문자열 -> Python 객체(dict or list)
'''

# json file(json 문자열) -> python dict 객체
print('json 객체 형식 읽기')
file = open("chapter08/data/usagov_bitly.txt", mode='r', encoding='utf-8')
#print(file.read()) # 전체 문서 읽기 
lines = file.readlines() # 줄단위 전체 읽기

# 줄 단위 읽기(json string) -> dict 객체 변환  -> list 저장 
rows = [  json.loads(row) for  row in lines  ]
#print(recodes) # [dict] 결과 확인 
# [{'a': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 ...]
print('rows :', len(rows)) # rows : 3560

# 전체 행 출력 
for row in rows[:10] :
    print(row)
    print(type(row))
    
file.close()

# dict -> DataFrame 변환
'''
 {} -> row, 'key:value' -> column
'''
import pandas as pd
recode_df = pd.DataFrame(rows)
print(recode_df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3560 entries, 0 to 3559
Data columns (total 18 columns):
'''





