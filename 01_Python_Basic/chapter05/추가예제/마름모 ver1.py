print("마름모 출력 프로그램 ver1.0")
print()
while True :
    count= int(input('홀수를 입력 하세요. (0 <- 종료) : '))
    if (count!=0) and (count%2!=0):
        count = int(count/2)+1
        for i in range(count) :
            print(' '*(count-i-1), end='')
            print('*'*(2*i+1))
    else:
        print("\n마름모 프로그램 출력을 이용해 주셔서 감사합니다")
        quit()