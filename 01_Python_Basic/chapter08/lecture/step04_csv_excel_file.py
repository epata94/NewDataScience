'''
csv, excel file 입출력
'''

import pandas as pd
import os

print(os.getcwd()) # C:\SUNMOON\3_Pywork-I\workspace\

# 1. csv 파일 읽기

###################
##  bmi.csv      ##
###################
bmi_data = pd.read_csv("chap07_FileIO/data/bmi.csv", encoding='utf-8')
print(bmi_data.info()) # str(data)
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20000 entries, 0 to 19999
Data columns (total 3 columns):
height    20000 non-null int64
weight    20000 non-null int64
label     20000 non-null object
'''
print(bmi_data.head())
print(bmi_data.tail())

# 칼럼 추출
height = bmi_data.height # 객체.칼럼명
weight = bmi_data['weight'] # 객체['칼럼명']
label = bmi_data['label']
print(len(label)) # 20000

# 키와 몸무게 평균
print('키 평균 : ', sum(height) / len(height)) # 키 평균 :  164.9379
print('몸무게 평균 : ', sum(weight) / len(weight)) # 몸무게 평균 :  62.40995

# 가장 큰 키와 몸무게
print('max height = ', max(height)) # max height =  190
print('max weight = ', max(weight)) # max weight =  85

# label 빈도수
label_count = {} # 빈 set

for key in label :
    label_count[key] = label_count.get(key, 0) + 1

print(label_count) # dict
# {'thin': 4898, 'normal': 7677, 'fat': 7425}

########################
### spam_data.csv : 제목명 없음
########################
spam_data = pd.read_csv("chap07_FileIO/data/spam_data.csv", header=None, encoding='ms949')
print(spam_data.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns):
0    5 non-null object
1    5 non-null object
'''
target = spam_data[0] # ham/spam
texts = spam_data[1] # message

print(target)
print(texts)

# target -> 더미변수(spam=1, ham=0)
target = [ 1 if t == 'spam' else 0 for t in target]
print(target) # [0, 1, 0, 1, 0]

# texts -> 텍스트 전처리(특수문자, 숫자, 공백, 영문 제거)
import re
def clean_text(text_string) :
    # 문장부호 제거
    texts_re = re.sub('[,.?!:;]', ' ', text_string)
    # 특수문자, 숫자 제거
    texts_re = re.sub('[@#$%^&]|[0-9]', ' ', texts_re)
    # 영문자 제거 : 소문자 변경 -> 제거
    texts_re = texts_re.lower() # 소문자 변경
    texts_re = re.sub('[a-z]', ' ', texts_re)
    # 공백 제거
    texts_re = ' '.join(texts_re.split())
    return texts_re

clean_text_re = [clean_text(t)  for t in texts]
clean_text_re
# ['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']


# 2. excel 파일 읽기 : 'xlrd' install
sam = pd.ExcelFile("chap07_FileIO/data/sam_kospi.xlsx")
# ImportError: Missing optional dependency 'xlrd'.
print(sam) # <pandas.io.excel._base.ExcelFile object at 0x1347FE50>

kospi = sam.parse("sam_kospi")
print(kospi) # [247 rows x 6 columns]
print(kospi.info())
'''
RangeIndex: 247 entries, 0 to 246
Data columns (total 6 columns):
'''

high = kospi['High']
low = kospi['Low']

from statistics import mean
print('high mean=', mean(high)) # high mean= 1307947.3684210526
print('low mean=', mean(low)) # low mean= 1280919.028340081












