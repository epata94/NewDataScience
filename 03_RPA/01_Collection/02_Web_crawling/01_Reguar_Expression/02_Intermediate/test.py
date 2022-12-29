import re

p = re.compile(r'\bis\b')
m = p.search('Cat is cute!')
print(m)

p = re.compile(r'\sis\s')
m = p.search('Cat is cute!')
print(m)

p = re.compile(r'\bis')
m = p.search('The island is there!')
print(m)

p = re.compile(r'\bis\b')
m = p.search('The island is there!')
print(m)

p = re.compile(r'\sis')
m = p.search('The island is there!')
print(m)

p = re.compile(r'\sis')
m = p.search('The island is there!')
print(m)
