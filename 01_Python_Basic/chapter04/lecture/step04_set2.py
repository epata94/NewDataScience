
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합 구하기
print(s1 & s2)
print(s1.intersection(s2))

# 합집합 구하기
print(s1 | s2)
print(s1.union())

# 차집합
print(s1-s2)
print(s1.difference(s2))

print(s2-s1)
print(s2.difference(s1))

# 교집합을 뺀 나머지
print( (s1 | s2) - (s1 & s2) ) # 합집합에서 교집합을 뺌
print(s1 ^ s2)                 # ^로 간단히 표현

# 집합의 공통여부 판단
if s1.isdisjoint(s2):
#if s1 & s2:
    print('s1과 s2는 같은 요소가 하나도 없습니다.')
else:
    print('s1과 s2는 같은 요소가 적어도 하나는 있습니다.')


