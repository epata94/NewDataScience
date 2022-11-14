import re

p = re.compile('ab{3}')
p = re.compile('abbb?')
m = p.search('abbb')
print(m)
m = p.search('a')
print(m)
m = p.search('abbbb')
print(m)
