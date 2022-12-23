import re
# positive look ahead
p = re.compile('01(?=0)')
m = p.search('010')
print(m)

p = re.compile('(?=0)10')
m = p.search('010')
print(m)

# positive look behind
p = re.compile('(?<=0)10')
m = p.search('010')
print(m)


