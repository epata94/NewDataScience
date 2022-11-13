# all은 iterable 객체 (2개 이상의 값을 담을 수 있는 자료형)에
# 적용가능하다.
# all 함수는 입력받은 데이터의 정합성을 체크할 때 사용할 수 있다.
print(all([1,2,3]))                         # 숫자형
print(all([1,2,0]))
print(all(['hello','world']))               # 문자열
print(all(['hello',' ']))
print(all(['hello','']))
print(all((1,2)))                           # 튜플
print(all((1,0)))
print(all({'조문수':'남','김혜경':'여'}))   # dictionary
print("Dictionary")
print(all({}))                              # dictionary
print(all(list({}.values())))                              # dictionary
# dictionary의 값은 Key, value 로 나누어서 확인
print(all(list({'조문수':'남','김혜경':''}.values())))                              # dictionary
print(all([1,'2',0.0]))                     # 복합자료형

result = [1,2,3].append(4) # 상수형 객체의 값을 변경하는 멤버함수사용은 주의
print(result)
print([1,2,3].append(4))
result = [1,2,3]
result.append(4)
print(result)

print([1,2,3].count(2)) # 상수형 객체의 값을 조회 하는 멤버함수는 가능
