import re
p=re.compile('[a-z]+')
m = p.match('python')
# m = p.search('3 python')
print(m)
if m:
    print('Match found:',m.group())
else:
    print('No match')

p=re.compile('[a-z]+')
m = p.match('3 python')
print(m)
