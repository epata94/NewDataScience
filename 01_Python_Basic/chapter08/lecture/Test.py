ftest = open('../data/ftest.txt', mode='r')
lines = ftest.readlines() #  줄 단위 전체 읽기 - list 반환
print(lines) # ['my first text~~~\n', 'my second text ~~~']
print(type(lines)) # <class 'list'>
print('문단 수 :', len(lines)) # 문단 수 : 2

# file 객체 -> 줄 단위 읽기
doc = []
# string.strip() : 문장 끝 불용어 처리(공백,제어문자 제거)
for line in lines:  # 'programming is fun\n'
    # print(line.strip())  # text만 출력
    print(line)  # text만 출력
    doc.append(line.strip())