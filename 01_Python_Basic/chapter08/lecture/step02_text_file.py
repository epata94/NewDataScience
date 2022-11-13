'''
텍스트 파일 입출력(file input/output)
 - 데이터 입출력 시(file, db) 반드시 예외 처리한다.
 형식) open('파일경로/파일명', mode='r' or 'w' or 'a')
        mode = 'r' : 파일 읽기
        mode = 'w' : 파일 쓰기
        mode = 'a' : 파일 쓰기 + 추가
'''

#open(file=, mode=, encoding=)
help(open)
# Help on built-in function open in module io:

import os
print(os.getcwd()) # D:\Pywork\workspace

# 1. 파일 입출력
try :
    # 1. 파일 읽기 : 현재 경로 = project 경로
    print('\n현재 경로 :', os.getcwd()) # 현재 경로 : D:\Pywork\workspace
    ftest1 = open('chapter08/data/ftest.txt', mode = 'r') # / or \\
    print(ftest1.read()) # 파일 전체 읽기
    print(type(ftest1.read()))

    # 2. 파일 쓰기(자동 생성)
    ftest2 = open('chapter08/data/ftest2.txt', mode = 'w')
    ftest2.write('my first text~~~') # 파일 쓰기

    # 3. 파일 쓰기(내용 추가)
    ftest3 = open('chapter08/data/ftest2.txt', mode = 'a')
    ftest3.write('\nmy second text ~~~') # 파일 쓰기(추가)

except Exception as e:
    print('Error 발생 : ', e)

finally:
    # 파일 객체 닫기
    ftest1.close()
    ftest2.close()
    ftest3.close()

# 2. 파일 읽기 관련 함수
try :
    ftest = open('chapter08/data/ftest.txt', mode='r')
    # (1) read() : 전체 텍스트 자료 읽기
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))

    # (2) readlines() : 줄 단위 읽기
    ftest = open('chapter08/data/ftest.txt', mode='r')
    lines = ftest.readlines() #  줄 단위 전체 읽기 - list 반환
    print(lines) # ['my first text~~~\n', 'my second text ~~~']
    print(type(lines)) # <class 'list'>
    print('문단 수 :', len(lines)) # 문단 수 : 2

    # file 객체 -> 줄 단위 읽기
    doc = []
    # string.strip() : 문장 끝 불용어 처리(공백,제어문자 제거)
    for line in lines:  # 'my first text~~~\n'
        print(line.strip())  # text만 출력
        doc.append(line.strip())

    print(doc)  # 문장

    # (3) readline() : 한 줄 읽기
    ftest = open('chapter08/data/ftest.txt', mode='r')
    line = ftest.readline() #  한 줄 읽기
    print(line)  # ['my first text~~~\n', 'my second text ~~~']
    print(type(line))  # <class 'list'>

except Exception as e:
    print('Error 발생 : ', e)

finally:
    # 파일 객체 닫기
    ftest.close()

# 3. with 블록과 encoding
try :
    # 형식) with open(파일 입출력) as 참조변수 :
    with open('chapter08/data/ftest3.txt', mode='w', encoding='utf-8') as  ftest : # 한글 사용
        ftest.write('파이썬 파일 작성 연습')
        ftest.write('\n파이썬 파일 작성 연습2')
        # with 블럭 벗어나면 자동 close
    with open('chapter08/data/ftest3.txt', mode='r', encoding='utf-8') as ftest :
        print(ftest.read())

except Exception as e:
    print('Error 발생 : ', e)

finally:
    pass


# exam01