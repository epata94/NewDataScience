
from re import match

# 2.match(pattern, string, flags)
# - 패턴 일치 여부 반환 : object 반환(일치) or NULL(불일치)

# (1) 패턴과 일치된 경우
jumin = '123456-3234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result) # <re.Match object; span=(0, 14), match='123456-1234567'>
# None = Null

if result : # object
    print('주민번호 일치') # 주민번호 일치
else : # null
    print('잘못된 주민번호')

# (2) 패턴과 불일치된 경우
jumin = '123456-5234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result) # <re.Match object; span=(0, 14), match='123456-1234567'>
# None = Null

if result : # object
    print('주민번호 일치') # 주민번호 일치
else : # null
    print('잘못된 주민번호')
