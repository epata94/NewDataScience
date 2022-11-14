import re
# p = re.compile(r'(\b\w+)\s+\1')
try:
    # p = re.compile(r'(\s\w+)\b+\1')
    p = re.compile(r'(\s\w+)\b\1')
    print('|',end='')
    print(p.search('Paris in the the spring. It It was really great').group(),end='')
    print('|')
except Exception as e:
    print(e)
# p = re.compile('(\b\w+)\s+\1')
