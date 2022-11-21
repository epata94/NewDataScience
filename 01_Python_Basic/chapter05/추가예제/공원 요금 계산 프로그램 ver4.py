age=int(input('나이를 입력 하여 주세요 : '))
price=0
grade=""
if (age>=0) and (age<4):
    grade="유아"
    print(f' 귀하는 {grade}등급이며 요금은 무료 입니다.')
    quit()
elif (age>=4) and (age<14):
    price=2000
    grade="어린이"
elif (age>=14) and (age<19):
    price=3000
    grade="청소년"
elif (age>=19) and (age<66):
    price=5000
    grade="성인"
elif age>=66:
    grade="노인"
    print(f'귀하는 {grade}등급이며 요금은 무료 입니다.')
    quit()
else:
    print("다시 입력 하세요")
    quit()

print(f' 귀하는 {grade}등급이며 요금은 {price} 입니다.')
pay=int(input("1: 현금, 2: 공원 전용 신용카드 >> "))
if pay==1:
    cash=int(input("요금을 입력 하세요"))
    if cash==price:
        print("감사합니다. 티켓을 발행 합니다.")
    elif cash>price:
        print(f"감사합니다 티켓을 발행하고 거스름돈 {cash-price}원을 반환 합니다.")
    else:
        print(f"{price - cash}원이 모자랍니다. 입력하신 {cash}를 반환 합니다.")
elif pay==2:
    if age>=60:
        price=int(price*0.85)
    else:
        price=int(price*0.9)
    print(f"{price}원 결제 되었습니다. 티켓을 발행합니다")
else:
    print("다시 입력 하세요")
    quit()


