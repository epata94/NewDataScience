while True:
    message=input("저장할 내용을 입력 하세요 ( 종료는 엔터 ) : ")
    if message!='':
        file = open('test.txt','a')
        file.write(message+'\n')
        file.close()
    else:
        break

file = open('test.txt','r')
print(file.read())
file.close()