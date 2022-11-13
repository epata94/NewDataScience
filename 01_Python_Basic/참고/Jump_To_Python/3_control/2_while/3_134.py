# coding: cp949

coffee = 10
money = 0
coffee_price = 300

while True:
    money = int(input("돈을 넣어 주세요: "))
    if money < coffee_price:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
    else:
        coffee = coffee -1
        if money > coffee_price:
            print("거스름돈 %d를 주고 "%(money-300), end='')
        print("커피를 줍니다.")
        
    print("남은 커피의 양은 %d개입니다.\n"%coffee)

    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

print("프로그램 종료")