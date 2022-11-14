import re

#p = re.compile('\') <= 정규식으로 표현이 불가능하다.
#p = re.compile('\\') <= 정규식으로 표현이 불가능하다.
p = re.compile('\\\\') #<= 정규식으로 표현이 불가능하다.

m=p.match('\\section')
print(m)

p = re.compile(r'\\')
m=p.match('\\section')
print(m)
m=p.match('\\\\section')
print(m)
p = re.compile(r'\\\\')
m=p.match('\\\\section')
