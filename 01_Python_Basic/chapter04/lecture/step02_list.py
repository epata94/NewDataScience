'''
list 특징
 - 1차원 배열 구조
     형식) list변수 = [값1, 값2,..]
 - 다양한 자료형 저장 가능  
 - index 사용(순서 있음)
     형식) list변수[index]  
 - 값 수정(추가,삽입,수정,삭제) 
'''

help(list) # Help on class list in module builtins:
# 1. 단일 list

# (1) 단일 list 예
lst = [1,2,3,4,5]
print(lst)
print(type(lst))
for i in lst :
    print(lst[:i]) # i 전까지
'''
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
'''

for i in lst :
    print(lst[i-1: ])
'''
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
[3, 4, 5]
[4, 5]
[5]
'''    


# (2) 단일 list 색인 
x = list(range(1, 11))
print(x)
print(x[:5]) # [1, 2, 3, 4, 5]
print(x[-5:]) # [96, 97, 98, 99, 100]
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] - 전체 
[1, 2, 3, 4, 5] - 처음 5개 
[6, 7, 8, 9, 10] - 최근 5개 
'''
print('index 2씩 증가 ')
print(x[::2]) # 홀수 
print(x[1::2]) # 짝수(index 1부터 시작) 
    
    
# 2. 중첩 list 생성

# (1) 단일 list 객체 생성
a = ['a', 'b', 'c']  # list 생성 
print(a)

# (2) 중첩 list 객체 생성 ㄴㄴ
b = [10, 20, a, 5, True, '문자열'] # 서로 다른 type 가능
print(b[0]) # 10
print(b[2]) # ['a', 'b', 'c'] -> 중첩 list 
print(b[2][0]) # a  -> 중첩 list 1번 원소 
print(b[2][1:]) # ['b', 'c'] -> 중첩 list 2번 이후 원소 

# 자료구조 확인
print(type(a), type(b)) # <class 'list'>
print(id(a), id(b)) # 40648584 40647432

# 3. 추가,삭제,수정,삽입
num = ['one', 'two', 'three', 'four']

print(num) # ['one', 'two', 'three', 'four']
print(len(num)) # 4

num.append('five') # 추가
print(num) # ['one', 'two', 'three', 'four', 'five']

num.remove('five') # 삭제 
print(num)

num[3] = '4' # 수정 
print(num)

num.insert(0, 'zero')  # 삽입 
print(num)  

# 4. list 연산
      
# list 결합 
x =  [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y  # new object
print(z) # [1, 2, 3, 4, 1.5, 2.5]

# list 확장 
x.extend(y)  # x 확장 
print(x) # [1, 2, 3, 4, 1.5, 2.5]

# list 추가 
x.append(y) # x 추가 
print(x) # [1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]]

# list 제곱  
lst = [1, 2, 3, 4] # list 생성

# lst 원소를 2개씩 생성하여 result 저장
result = lst * 2 # 각 원소 연산 안됨 
print(result) # [1, 2, 3, 4, 1, 2, 3, 4]

# list 사칙연산 : 원소 대상 
print('1.5 * 2 = ', y[0] * 2) # 1.5 * 2 =  3.0
'''
list는 전체 원소 연산 불가 = 선형대수 연산 불가 
선형대수 : 벡터와 행렬 대상 수학적 연산 
'''

# 5. list 정렬과 원소 찾기
print(result) # [1, 2, 3, 4, 1, 2, 3, 4]
result.sort() # 오름차순 정렬 
print(result) #[1, 1, 2, 2, 3, 3, 4, 4]
result.sort(reverse = True) # 내림차순 정렬 
print(result) # [4, 4, 3, 3, 2, 2, 1, 1]

# 6. list에서 원소 찾기

'''
if '원소' in list : 
    참 실행문 : list에 '원소' 포함 
else :
    거짓 실행문 : 미 포함 
'''

import random

r = []
for i in range(5) :
    r.append(random.randint(1,5))

print(r)
    
if 4 in r :
    print('있음')
else :
    print('없음')

'''
scala vs vector 
scala 변수 : 한 개의 값[상수]를 갖는 변수(크기)
vector 변수 : 다수의 값을 갖는 변수(크기와 방향)
'''

print('\nvector 값 추가')
dataset = []  # 빈 list
cnt = 0
while cnt < 5:  # 5개 추가
    dataset.append(cnt + 5)  # 추가할 값
    cnt += 1

print(dataset)  # [5, 6, 7, 8, 9]

# exam01

'''
7. 리스트 내포 
 - list에 for문 포함 
 형식1) 변수 = [ 실행문  for   ]
 실행순서 : 1.for문 > 2.실행문 > 3.변수 저장
 형식2) 변수 = [ 실행문  for  if ]
 실행순서 : 1.for문 > 2.if > [3.실행문 > 4.변수 저장] 
'''

# 형식1) 변수 = [ 실행문  for   ]
# x변량에 제곱 계산
x = [2,4,1,5,7]
# print(x ** 2) # error

lst = [ i ** 2   for i in x ]
print(lst) # [4, 16, 1, 25, 49]


# 형식2) 변수 = [ 실행문  for  if ]
# 1~10 -> 2의 배수 추출 -> i*2 -> list 저장
num = list(range(1,11))

lst2 = [ i*2  for i in num  if i % 2 == 0  ]
print(lst2)
# [4, 8, 12, 16, 20]