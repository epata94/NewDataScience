import io

def write(message):
    with open("data/메세지.txt", mode='w',encoding='utf-8') as messages:
        for i in range(1,11):
            messages.write(message+f"{i}\n\n")

message = input("메시지를 입력하세요: ")
write(message)
