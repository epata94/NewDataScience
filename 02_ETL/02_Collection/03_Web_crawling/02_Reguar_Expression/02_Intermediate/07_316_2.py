import re
p = re.compile('.+:')
p = re.compile('.+(?=:)')
m = p.search('http://google.com')
m = p.search('https://google.com')
m = p.search('http//google.com')
print(m.group())