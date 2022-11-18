#3.	다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트(test03_myargv.py)를 작성해 보자.
import sys


def Sum(num):
    sum = 0
    for i in num:
        sum += int(i)

    return sum

num = sys.argv[1:]
print(Sum(num))