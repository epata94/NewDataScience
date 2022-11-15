def print_5xn(message):
    for i in range(0,len(message),5):
        print(message[i:i+5])

message=input("메세지를 입력 하여 주세요 : ")
print_5xn(message)