'''
- 얕은 복사, 깊은 복사 
'''
# 자료구조 복사

# 1. 얕은 복사 : 주소 복사(내용, 주소 동일)
name = ['홍길동', '이순신', '강감찬']
print('name address =', id(name)) # name address = 2049488

name2 = name # 주소 복사
print('name2 address =', id(name2)) # 5916112 5916112

print(name)
print(name2)

# 원본 수정
name2[0] = "김길동" # 수정 : 원본/사본 수정  
print(name)
print(name2)
# ['김길동', '이순신', '강감찬'] ['김길동', '이순신', '강감찬']


# 2. 깊은 복사 : 내용 복사(내용 동일, 주소 다름)
import copy 
name3 = copy.deepcopy(name)
print(name)
print(name3)

print('name address =', id(name)) # 2049488
print('name3 address =', id(name3)) # 6933520

# 원본 수정 
name[1] = "이순신장군"
print(name)
print(name3)
'''
['김길동', '이순신장군', '강감찬']
['김길동', '이순신', '강감찬']
'''

















