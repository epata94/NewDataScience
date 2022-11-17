def search_visitor(name):
    try:
        guest_book= open('D:/Pywork/DataScience/pythonBasic/Chapter8/Test/방명록.txt', encoding="UTF8")
        read_guest_book=guest_book.read()
        if read_guest_book.find(name)==-1:
            return -1
        return name

    except Exception as e:
        print(f"에러발생: {e}")
    finally:
        guest_book.close()


name=input("이름을 입력하세요: ")
if search_visitor(name)==-1:
    birth=input("생년월일을 입력하세요 (예:801212): ")
    input_data=name+" "+birth
    print(f'{name}님 환영합니다. 아래 내용을 입력하셨습니다')
    print(input_data)
    try:
        guest_book= open('D:/Pywork/DataScience/pythonBasic/Chapter8/Test/방명록.txt',mode='a', encoding="UTF8")
        guest_book.write("\n"+input_data)
    except Exception as e:
        print(f"에러발생: {e}")
    finally:
        guest_book.close()
else:
    print(f'{name}님 다시 방문해주셔서 감사합니다. 즐거운 시간되세요')
