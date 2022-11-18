message=input("메시지를 입력하세요: ")
try:
    with open("메세지.txt",mode='a') as file:
        for i in range(1,11):
            file.write(message+str(i)+'\n')
except Exception as e:
    print(f'ERROR: {e}')


with open("메세지.txt") as read_file:
    print(read_file.read())