'''
csv, excel file read
 - 칼럼 단위로 작성된 excel 파일 유형 읽기
 
CMD에서 pandas 패키지 install
- pip install pandas
- pandas, numpy, pytz, deteutil, six 패키지 install   
'''

'''
csv, excel file 입출력
'''

import pandas as pd
import os

print(os.getcwd()) # C:\SUNMOON\3_Pywork-I\workspace\

# 1. csv 파일 읽기

###################
##  score.csv      ##
###################
score = pd.read_csv("chapter08/data/score.csv")
print(score.info()) # str(data)

print(score.head())

# 칼럼 추출
kor = score.kor # 객체.칼럼명
eng = score['eng'] # 객체['칼럼명']
mat = score['mat']
dept = score['dept']

# 과목별 최고 점수
print('max kor = ', max(kor)) # max height =  190
print('max eng = ', max(eng)) # max weight =  85
print('max mat = ', max(mat))

# 과목별 최하 점수
print('min kor = ', min(kor)) # max height =  190
print('min eng = ', min(eng)) # max weight =  85
print('min mat = ', min(mat))

# 과목별 평균 점수
from statistics import mean
print('국어 점수 평균 : ', round(mean(kor),3))
print('영어 점수 평균 : ', round(mean(eng),3))
print('수학 점수 평균 : ', round(mean(mat),3))


# dept 빈도수
dept_count = {} # 빈 set

for key in dept :
    dept_count[key] = dept_count.get(key, 0) + 1

print(dept_count) # dict
# {101: 5, 102: 5, 103: 5}

# 정규화 (0~1)
'''
height_nor = [ h/190 for h in height ]
weight_nor = [ w/85 for w in weight ]
print(height_nor[:10])
print(weight_nor[:10])

print('height mean : ', round(sum(height_nor) / len(height_nor),2) )
print('weight mean : ', round(sum(weight_nor) / len(weight_nor),2) )
'''
'''
height mean :  0.87
weight mean :  0.73
'''



##############################
### spam_data.csv : 제목 없음
##############################
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
sam = pd.ExcelFile("chapter08/data/sam_kospi.xlsx")
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

print('High mean :', high.mean())
print('Low mean :', low.mean())

'''
High mean : 1307947.3684210526
Low mean : 1280919.028340081

기타 통계, 차트 시각화 Python2에서  
'''

# exam03