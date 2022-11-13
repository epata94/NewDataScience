'''
tuple 특징 
 - 순서존재(index 사용 가능)
 - 수정 불가
 - 문자열 원소 표현 
 - list 속도 빠름 
 - 제공 함수 없음 
 형식) (원소1, 원소2, ...n) : () 생략 
'''


help(tuple) # Help on class tuple in module builtins:

# 단일 인수
t = 10 ; t1 = (10, )
t = (10)

print(t)
print(t, t1) # 10 (10,)

# 여러개 인수
t2 = (1,2,3,4,5,3)
print(t2) # (1, 2, 3, 4, 5, 3)

# index
print(t2[0], t2[1:4], t2[-1]) # 1 (2, 3, 4) 5

#  수정 불가 
# t2[0] = 10 # error

print()

for i in t2 :
    print(i, end=' ')

# 요소 검사
if 6 in t2 :
    print("6 있음")
else :
    print("6 없음")

# tuple 함수
lst = list(range(1,6))
t3 = tuple(lst)
print(t3) # (1, 2, 3, 4, 5, 3)
print(len(t3), type(t3)) # 5 <class 'tuple'>
print(t3.count(3)) # 2
print(t3.index(4)) # 3

