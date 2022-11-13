print("마름모 출력 프로그램 ver1.0\n")

while True:

    odd_number = int(input("홀수를 입력하세요(0 <- 종료): "))

    if (odd_number == 0):
        print("마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break
    else:
      for star in range(1, (odd_number+1)//2+1):
        print(' '*((odd_number+1)//2-star) + '*'*(2 * star -1))


