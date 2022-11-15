def print_5xn(message):
    for i in range(0,len(message),5): # 시작,전체 글자수로 끝 인덱스, i 값 5 증가
        print(message[i:i+5]) # 5증가한 값 들씩 부터 +5글자씩 까지 출력

message=input("다섯 글자씩 잘라낼 메세지를 입력 하여 주세요 : ")
print_5xn(message)