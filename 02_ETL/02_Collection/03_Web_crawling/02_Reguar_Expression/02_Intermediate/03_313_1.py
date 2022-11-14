import re
p=re.compile(r'(\w+)\s+(\d+)[-](\d+)[-](\d+)')

m = p.match("park 010-1234-5678")
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(4))
# print(m.group(5)) group 5는 지정되어 있지 않기 때문에 에러를 발생한다.
