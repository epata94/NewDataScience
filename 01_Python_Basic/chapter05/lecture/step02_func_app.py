'''
텍스트 전처리 함수 정의
'''

# 텍스트 전처리2
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

import re

# 1. 텍스트 전처리
def clean_text(text_string):
    # 문장부호 제거
    text_string_re = re.sub('[,.?!:;]', '', text_string)
    # 특수문자, 숫자 제거 
    text_string_re = re.sub('[!@#$%^&*()]|[0-9]', '', text_string_re)
    # 영문 소문자 -> 영문 제거 
    text_string_re = text_string_re.lower()
    text_string_re = re.sub('[a-z]', '', text_string_re)
    # 공백 제거
    text_string_re = ' '.join(text_string_re.split()) # '우리나라 대한민국'
    
    return text_string_re
     
# 함수 호출 : [실행문 for ] 
text_string_re = [clean_text(string)  for string in texts]    
print('텍스트 전처리 후 ')
print(text_string_re) 
# ['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']



# 2. 표본의 분산/표준편차

dataset = [2,4,5,6,1,8]

'''
분산 = (sum(x변량-산술평균)**2)) / (n-1)
표준편차 = sqrt(분산)
'''

from statistics import mean, variance
from math import sqrt

# 산술평균  
def Avg(data):
    avg = mean(data)
    return avg

print('산술평균 =', Avg(dataset))
# 산술평균 = 4.333333333333333

# 분산/표준편차 
def var_sd(data): # [2,4,5,6,1,8] - avg
    avg = Avg(data) # 함수 호출
    # list 내포
    diff = [ (d - avg)**2  for d in data]
    
    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)
    
    return var, sd

v, s = var_sd(dataset)
print('분산 =', v)
print('표준편차=', s)
'''
분산 = 6.666666666666666
표준편차= 2.581988897471611
'''
print('내장함수 분산 =', variance(dataset))
# 내장함수 분산 = 6.666666666666666
    
# 2) 파타고라스 정리
def pytha(s, t) :
    a = s**2 - t**2
    b = 2 * s * t
    c = s**2 + t**2
    print("피타고라스의 정리 : 3변의 길이 : ",a,b,c)

pytha(2, 1)
    
9+16 # 25

# 3) 몬테카를로 시뮬레이션
import random
help(random.randint)

# 단계 1 : 동전 앞면과 뒷면의 난수 확률분포 함수 정의
def coin(n) :
    result = []
    for i in range(n) :
        r = random.randint(0, 1)
        if (r == 1) :
            result.append(1) # 앞면
        else :
            result.append(0) # 뒷면
    return result

print(coin(10)) # [0, 1, 1, 0, 1, 0, 0, 1, 0, 1]


# 단계 2 : 몬테카를로 시뮬레이션 함수 정의
def montaCoin(n) :
    cnt = 0
    for i in range(n) :
        cnt += coin(1)[0] # coin 함수 호출

    result = cnt / n # 동전 앞면과 뒷면의 누적 결과를 시행 횟수(n)로 나눈다.
    return result

#단계 3 : 몬테카를로 시뮬레이션 함수 호출
print(montaCoin(10)) # 0.3
print(montaCoin(30)) # 0.5666667
print(montaCoin(100)) # 0.53
print(montaCoin(1000)) #  0.51
print(montaCoin(10000)) # 0.5033