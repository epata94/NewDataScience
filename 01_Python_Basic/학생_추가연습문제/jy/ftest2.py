#2.	본인의 공유 폴더에 ‘메세지.txt’ 파일을 생성하고 파일에 아래와 같은 메시지를 입력받아 저장한다.

file = open("//192.168.0.47/데이터분석_수업/송지예/1118/메세지.txt", mode="w")
msg = input("메세지를 입력하세요: ")
for i in range(10):
    file.write(f"{msg}{i+1}\n\n")
