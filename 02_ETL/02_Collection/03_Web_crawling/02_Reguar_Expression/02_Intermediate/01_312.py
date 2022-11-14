import re

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK? ABC')
print(m)
print(m.group(0))
print(m.group(1))

m = p.search('ABCABCAB OK?')
print(m)

p = re.compile('(김혜경)+')
m = p.search('김혜경김혜경 OK?')
print(m)

m = p.search('김혜경김혜경 우리 막내 김혜경!')
print(m)
print(m.group(0))
print(m.group(1))
# print(m.group(2))
