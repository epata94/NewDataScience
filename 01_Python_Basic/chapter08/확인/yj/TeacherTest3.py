# 3.	다음과 같은 내용을 지닌 파일 life.txt가 있다.
# 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# Life is too short
# you need java

try:
    life_file = open('D:/Pywork/DataScience/pythonBasic/Chapter8/Test/life.txt')
    text=life_file.read()
    text=text.replace('java','python')
    life_file = open('D:/Pywork/DataScience/pythonBasic/Chapter8/Test/life.txt',mode='w')
    life_file.write(text)
except Exception as e:
    print(f'ERRPR: {e}')
finally:
    life_file.close()