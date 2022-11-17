try :
    str = None
    print('저장할 내용을 입력하세요(종료는 엔터)')
    while str != '' :
        file = open("test2.txt", mode= 'a', encoding= 'UTF-8')
        str = input()

        file.write(str+'\n')
        file.flush()
except Exception as e:
    print('Error 발생 : ', e)
finally:
    file.close()
