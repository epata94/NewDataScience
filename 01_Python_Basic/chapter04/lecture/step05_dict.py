'''
dict 특징 
  - set 자료구조와 유사함
  형식) {'key':value, 'key':value, ...}
  - json 형식, R의 list 동일
  - key 접근만 가능함(index, value 사용 불가)
  - key 중복 불가 
  - 출력 순서 random
'''

# dict 생성 방법1
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic) # {'key2': 200, 'key1': 100, 'key3': 300}

# dict 생성 방법2
person = {'name':'홍길동', 'age': 35, 'address' : '서울시'}
print(person)
print( person['name']) # index : key

print(type(dic), type(person)) # <class 'dict'> <class 'dict'>

# 원소 수정, 삭제, 추가
# dict 원소 수정 
person['age'] = 45
print(person)

# dict 원소 삭제
del person['address']
print(person) # {'name': '홍길동', 'age': 45}

# dict 원소 추가 
person['pay'] = 350
print(person) # {'name': '홍길동', 'pay': 350, 'age': 45}


# 요소 검사
print(person['age']) # 35
print('age' in person) # True

# 요소 반복
for key in person.keys() : # key 넘김 
    print(key) # key 출력 

for v in person.values() : # value 넘김 
    print(v) # value 출력  

for i in person.items() : # item 넘김 
    print(i) # ('name', '홍길동')


# 키로 값 가져오기 : get(key)
print( person['name']) # index 형식
print( person.get('name')) # get함수 -> 홍길동 

# 내용 지우기 obj.clear()
person.clear()
print(person) # {}

#  {key : [val1, val2]} - {'영화' : [평점, 관객수]}
movie = {'광해' : [9.24, 1200], '공작' : [7.86, 500], '관상' : [8.01, 900],}
 
for r in movie.items() :
    print(r)
'''
('광해', [9.24, 1200])
('공작', [7.86, 500])
('관상', [7.98, 900])
'''
for r, d in movie.items() :
    print(r, d)    
'''
광해 [9.24, 1200]
공작 [7.86, 500]
관상 [8.01, 900]
'''

#  문] 평점 8이상인 영화 제목과 누적관객수 출력하기 
'''
광해
관상
누적 관객수 =  2,100
'''    
tot = 0
for r, d in movie.items() :
    if d[0]  >= 8.0 :
        print(r)  # 광해 관상
        tot += d[1]
print('누적 관객수 = ', format(tot, '3,d'))

print('emp')
emp = {'hong' : 350, 'lee' : 450, 'kang' : 550}
print(emp)
print(emp['lee'])
print(emp.get('hong')) # 350

# dict 원소 수정 
emp['lee'] = 300
print(emp)

# dict 원소 제거 
del emp['hong']
print(emp) 

# dict 원소 추가 
emp['yoo'] = 250
print(emp) # {'lee': 300, 'kang': 550, 'yoo': 250}

'''
key = input('찾을 키 : ')

# 형식) if value in object :
if key in person :  
    print(key + ' 있어요')
    print(person[key])
else :
    print(key + ' 없어요')
'''

if 'kang' in emp : 
    print('있음')
else : 
    print('없음')


for name, pay in emp.items():
    print(f"name : {name} => pay {pay}")
    
# [실습] 문자 빈도수 구하기[1] 
charset = ['abc', 'code', 'band', 'band', 'abc']
wc = {}

for ch in charset :
    if ch in wc :
        wc[ch] += 1 # key이용 : 수정  
    else :
        wc[ch] = 1
        
print(wc) # {'a': 1, 'c': 0, 'b': 1}

# 최고 출현 단어
print('max = ', max(wc, key=wc.get)) # max =  a

# 출현 빈도수 단어 정렬
print(sorted(wc, key=wc.get, reverse=True)) # ['a', 'b', 'c']
print(sorted(wc, key=wc.get)) # ['c', 'a', 'b']


# [실습] 문자 빈도수 구하기[2]
charset = ['abc', 'code', 'band', 'band', 'abc']
wc = {}

for key in charset : 
    # get()함수 : key 이용 value 가져오기 
    wc[key] = wc.get(key, 0) + 1 # get() 이용
    

print(wc)
'''
get(key, 0) + 1 
 - 해당 key의 값이 없으면 0, 있으면 기존 값에 +1 
'''

# #exam04    








