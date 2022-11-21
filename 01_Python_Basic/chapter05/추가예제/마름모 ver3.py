print("마름모 출력 프로그램 ver1.0")
print()
while True :
    count= int(input('홀수를 입력 하세요. (0 <- 종료) : '))
    line="-"*count
    if (count!=0) and (count%2!=0):
        print(line)
        count = int(count/2)+1
        for i in range(count) :
            print("|",end='')
            print(' '*(count-i-1), end='')
            print('*'*(2*i+1),end='')
            print(' ' * (count - i - 1), end='')
            print("|")
        for j in range(count-2,-1,-1):
            print("|", end='')
            print(' ' * (count - j - 1), end='')
            print('*'*(2*j+1),end='')
            print(' ' * (count - j - 1), end='')
            print("|")
        print(line)
    else:
        print("\n마름모 프로그램 출력을 이용해 주셔서 감사합니다")
        quit()