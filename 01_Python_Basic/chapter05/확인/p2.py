# 2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
def avg_numbers(*args):
    result = 0

    for i in args:
        result += i

    return result / len(args)


numbers = []

length = int(input('입력실 숫자의 개수 : '))

for i in range(length):
    numbers.append(int(input(f'{i + 1}번째 숫자 : ')))

print(f'입력하신 숫자들의 평균은 {avg_numbers(*numbers)}입니다.')
