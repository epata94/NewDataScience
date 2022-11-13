number = 0
while True:
    input_number = int(input("홀수를 입력하세요 (0 <- 종료): "))
    space = input_number / 2
    space = int(space)
    star = 1
    if input_number == 0:
        print("\n마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break
    while True:
        print(" " * space, end='')
        print('*' * star)
        space = space - 1
        if star >= input_number:
            break
        star = star + 2
