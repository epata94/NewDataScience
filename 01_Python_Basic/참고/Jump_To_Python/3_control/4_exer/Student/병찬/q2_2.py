number = 0
invert = 1
while True:
    input_number = int(input("홀수를 입력하세요 (0 <- 종료): "))
    space = input_number / 2
    space = int(space)
    star = 1
    invert = 1
    if input_number == 0:
        print("\n마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break
    while True:
        print(" " * space, end='')
        print('*' * star)
        if star == input_number:
            invert = -1
        star = star + (2 * invert)
        space = space - (1 * invert)
        if star < 1:
            break
