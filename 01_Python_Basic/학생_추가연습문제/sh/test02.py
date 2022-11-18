with open('//192.168.0.47/데이터분석_수업/임성혁/1118/메모장.txt', 'w', encoding='UTF-8') as file:
        message = input("메세지를 입력 하세요 : ")
        for i in range(1, 10):
            file.write(f'{message}{i}\n')
            print(f'{message}{i}')
