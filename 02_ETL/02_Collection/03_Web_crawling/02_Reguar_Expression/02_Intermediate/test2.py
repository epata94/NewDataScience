import re

p = re.compile('\d$')
m = p.match('dfs 1')
print(m)

