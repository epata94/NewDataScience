st1 = '1234 abc홍길동 ABC_555_6 이사도시'
st2 = 'test1abcABC 123mbc 45test'
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

import re # 정규표현식 모듈 - 방법1
from re import findall, match, sub # - 방법2

# 1. findall('pattern', string) -> list 반환

# 1) 숫자 찾기
print(findall('1234', st1, flags=0)) # ['1234']
print(findall('[0-9]', st1)) # ['1', '2', '3', '4', '5', '5', '5', '6']
print(findall('[0-9]{3}', st1)) # ['123', '555']
print(findall('[0-9]{3,}', st1)) # ['1234', '555']
print(findall('\\d{3,}', st1)) # ['1234', '555']

# 2) 문자열 찾기
print(findall('[가-힣]{3,}', st1)) # 이름 찾기 - ['홍길동', '이사도시']
print(findall('[a-z]{3}', st1)) # ['abc']
print(findall('[a-z|A-Z]{3}', st1)) # ['abc', 'ABC']

# 단어에서 한글 이름 찾기
st_list = st1.split()
print(st_list) # ['1234', 'abc홍길동', 'ABC_555_6', '이사도시']

names = [] # 이름 저장
for st in st_list : # 'abc홍길동'
    name = findall('[가-힣]{3,}', st) # 'abc홍길동' -> ['홍길동']

    if name : # 1개 이상 원소
        #names.append(name) # [ ['홍길동'] ] -> 중첩list
        names.append(name[0]) # ['홍길동', '이사도시']

print('names :', names) # names : ['홍길동', '이사도시']


# 3. 문자열 찾기
st2 = 'test1abcABC 123mbc 45test'

# 접두어/접미어
print(findall('^test', st2)) # 접두어 - ['test']
print(findall('st$', st2)) # 접미어 - ['st']

# 종료 문자 찾기 : abc, mbc
print(findall('.bc', st2)) # ['abc', 'mbc']

# 시작 문자 찾기
print(findall('t.', st2)) # ['te', 't1', 'te']


# 4. 단어 찾기(\\w) - 한글,영문,숫자
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

words = findall('\\w{3,}', st3)
print(words) # ['test', '홍길동', 'abc', '123', 'tbc']


# 5. 문자열 제외 : x+(x가 1개 이상 반복)
print(findall('[^t]+', st3)) # ['es', '^홍길동 abc 대한*민국 123$', 'bc']
# 특수문자 제외
print(findall('[^^*$]+', st3))
