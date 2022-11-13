odd = 1
star = 0
space = 0
plus_minus = 1

print("마름모 출력 프로그램 ver2.0")

while True:
    odd = int(input("홀수를 입력하세요(0 <- 종료): "))
    if odd == 0:
        break
    space = int(odd/2)
    star = 1
    plus_minus = 1

    while star != -1:
        print(" " * space + "*" * star)
        star = star + (2 * plus_minus)
        space = space - plus_minus

        if space < 0:
            space += 2
            star -= 4
            plus_minus = plus_minus * (-1)

    print("")