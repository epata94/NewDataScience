'''
문자열 특징
 - 문자들의 집합
 - 순서(index)를 갖는다.
 - 문자열 처리 함수 제공
'''

# 1. 문자열 유형
oneLine = "this is one line string" # 'this is one line string'
multiLine = """this is
multi line
string"""
multiLine2 ="this is\nmulti line\nstring"

print(oneLine)
print(multiLine)
print(multiLine2)

# 2. 색인과 문자열 연산 : +, *

# 1) 문자열 색인
string = "PYTHON"
print(string[0])
print(string[5])
print(string[-1])
print(string[-6])

# 2) 문자열 연산
print("python" + " program") # 결합연산자
# python-3.7.exe
#print("python-" + 3.7 + ".exe") # error
print("python-" + str(3.7) + ".exe") # python-3.7.exe

print("-"*30) # 반복연산자

# 3) 문자열 슬라이싱(slicing)
# lineStr = "this is one line string"

# 왼쪽 기준
print(oneLine)
print("문자열 길이 : ", len(oneLine))
print(oneLine[0:4]) # 1~4문자[start:end-1] - this
print(oneLine[:4]) # [:end-1] : 처음부터 ~
print(oneLine[:]) # 전체 원소 : this is one line string
print(oneLine[::2]) # 2의 배수 index : ti soeln tig

# 오른쪽 기준
print(oneLine[0:-1:2])
print(oneLine[-6:-1]) # strin
print(oneLine[-1:-6:-2])
print(oneLine[-6:]) # [start:end] - string

# 부분 문자열 생성
subString = oneLine[-11:]
print(subString) # line string


# 4) 문자열 처리 함수
# 특정 글자 수 반환
oneLine = "this is one line string"
print('t 글자 수 : ', oneLine.count('t'))

# 접두어 문자 비교 판단
print(oneLine.startswith('this'))
print(oneLine.startswith('that'))

# 문자열 교체
print(oneLine.replace('this', 'that'))

# 문자열 분리(split) : 문단 -> 문장
multiLine = """this is
multi line
string"""
sent = multiLine.split('\n')
print('문장 : ', sent)
# ['This ', 'is multi line', 'string']

# 문자열 분리(split)2 : 문장 -> 단어
words = oneLine.split(' ')  # split(sep = ' ') : default
print('단어 :', words)  # ['this', 'is', 'one', 'line', 'string']

'''
형태소 분석 : 문장 성분 분석(명사, 수사, 조사, 부사 등) - Python2에서 
'''

# 문자열 결합(join) : 단어들 -> 문장
sent2 = ','.join(words) # '구분자'.join(string) : 'this is',
print(sent2) # this,is,one,line,string
print(type(sent2))
