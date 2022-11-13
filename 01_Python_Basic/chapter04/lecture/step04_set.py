'''
set 특징
 - 순서 없음, 중복 허용 불가
 형식) 변수 = {값1, 값2,...} 
 - 집합 개념 
'''

# 중복 불가
s = {1,3,5,3,1}
print(len(s)) # 3
print(s) # {1, 3, 5}

# for + set 이용
for d in s :
    print(d, end=' ')  # 1 3 5
print()

# 집합관련 함수
s2 = {3, 6}
print(s.union(s2)) # 합집합 : s + s2 = {1, 3, 5, 6}
print(s.difference(s2)) # 차집합 : s - s2 = {1, 5}
print(s.intersection(s2)) # 교집합 : {3}

# 추가, 수정, 삭제 함수
s3 = {1, 3, 5}
print(s3)

s3.add(7) # 원소 추가 
print(s3) # {1, 3, 5, 7}

s3.update([5, '다섯'])
print(s3)

s3.discard(3) # 원소 삭제
print(s3) # {1, 5, 7}


# 중복 데이터 제거
gender = ['남','여','남','여']
sgender = set(gender) # list -> set
lgender = list(sgender) # set -> list
print(lgender) # ['남', '여']

print(lgender[1])




