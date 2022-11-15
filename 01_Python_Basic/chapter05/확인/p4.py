#4. 세 개의 숫자를 입력받아 가장 큰 수를 출력하는 print_max 함수를 정의하라
def print_max(n1, n2, n3):
    if(n1 > n2) :
        if(n1 > n3) :
            print(n1)
        else:
            print(n3)
    else :
        if(n2 > n3) :
            print(n2)
        else:
            print(n3)

n1 = int(input('숫자를 입력해주세요 : '))
n2 = int(input('숫자를 입력해주세요 : '))
n3 = int(input('숫자를 입력해주세요 : '))

print_max(n1, n2, n3)
