import os
import os.path
print(os.getcwd())

msg = input("메시지를 입력하세요 : ")

with open("메세지.txt", mode="w", encoding="UTF-8") as file:

    for m in range(1,11):
        file.write(f"{msg}{m}\n")


