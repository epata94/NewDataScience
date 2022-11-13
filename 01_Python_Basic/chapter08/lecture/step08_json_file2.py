'''
json 파일 형식(2가지)  

 1. 중괄호 : dict 형식 문자열, 순서없음 
    예) {key : value} - usagov_bitly.txt
    json.loads() : dict 형식 문자열 -> python dict 

 2. 대괄호 : list형식 문자열, 순서있음 
    예) [{key : value}, {key : value}] - labels.json
    json.load() : list 형식 문자열 -> python list 
'''

import json
import pandas as pd

#1. dict 형식 문자열 -> dict 
print('dict 형식 문자열')
file = open("../data/usagov_bitly.txt", mode='r', encoding='utf-8')

# 줄 단위 읽기(json string) -> dict 객체 변환  -> list 저장 
recodes = [  json.loads(row) for  row in file  ]
print(len(recodes)) # 3560
file.close()

#2. list 형식 문자열 -> list 
print('2. list 형식 문자열 ')
file2 = open("../data/labels.json", mode='r', encoding='utf-8')
print('file2')
print(file2) # file info
#print(file2.read()) # 전체 문서 읽기 
'''
[
  {
    "id": 76811,
    "url": "https://api.github.com/repos/pandas-dev/pandas/labels/Bug",
    "name": "Bug",
    "color": "e10c02",
    "default": false
  },
]
[해설] 대괄호는 순서 있는 배열[row], 중괄호는 순서 없는 객체[column]
'''

# json.load(file 객체)  file 객체 ->  list 객체 변환 
recodes2 = json.load(file2) 
print(type(recodes2)) # <class 'list'>
#print(recodes2) 
# [{'id': 76811, 'url': 'https://api.github.com/repos/pandas-dev/pandas/labels/Bug', ...]
print('rows :', len(recodes2)) # rows : 30

# dict 자료 보기
for row in recodes2 :
    print(row) # {'id': 76811, 'url': 'https://api.github.com/repos/pandas-dev/pandas/labels/Bug', 'name': 'Bug', 'color': 'e10c02', 'default': False}
    #print(type(row)) # <class 'dict'>

file2.close()

# 3. DataFrame 변환 : dict - DF
recode_df = pd.DataFrame(recodes2)
print(recode_df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30 entries, 0 to 29
Data columns (total 5 columns):
color      30 non-null object
default    30 non-null bool
id         30 non-null int64
name       30 non-null object
url        30 non-null object
dtypes: bool(1), int64(1), object(3)
'''
print(recode_df)
print(recode_df.ix[0:4, 'color':'name'])
'''
    color  default      id         name
0  e10c02    False   76811          Bug
1  4E9A06    False   76812  Enhancement
2  FCE94F    False  127681     Refactor
3  75507B    False  129350        Build
4  3465A4    False  134699         Docs
'''