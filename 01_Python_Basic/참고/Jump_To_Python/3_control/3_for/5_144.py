# coding: cp949
# Step1] 파이썬 기본 문법
a = [1,2,3,4]
result = []

for num in a:
    result.append(num*3)
print(result)

a=[1,2,3,4]
result = [num * 3 for num in a]
print(result)

a=[1,2,3,4]
result = [num * 3 for num in a if num %2 == 0]
print(result)
