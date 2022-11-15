# 1.주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수를 작성해 보자

def is_odd(number):
    if number % 2 == 0:
        return False

    return True


number = int(input('숫자를 입력하세요 : '))

if is_odd(number):
    print('홀수')
else:
    print('짝수')
