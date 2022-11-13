multiline ="""
안녕하세요. 파이썬 세계에 오신걸 
환영합니다.
열심히 공부합시다!
"""

count = 0
line_list = []
word_list = []

for line in multiline.split('\n'):
    line_list.append(line)
    for word in line.split(" "):
        word_list.append(word)
        print(word)

        count += 1

print('단어수:', count)
print(line_list)
print(word_list)
