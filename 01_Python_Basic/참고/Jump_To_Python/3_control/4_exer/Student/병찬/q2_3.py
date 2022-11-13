while True:
    input_number = int(input("홀수를 입력하세요 (0 <- 종료): "))
    space = int(input_number / 2)
    star = invert = 1
    if input_number == 0:
        print("\n마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break
    while star > 0:
        print(" " * space + '*' * star)
        if star == input_number: invert = -1
        star, space = (star + (2 * invert), space - (1 * invert))
