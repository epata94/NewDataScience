#coding:cp949

my_class = ""
charge = {"유아":0, "어린이":2000, "청소년":3000, "성인":5000, "노인":0}
payment=0
payment_way = 0
turn=0
free_ticket=5
annual_member_coupon=3

while True:
    age = int(input("나이를 입력하세요: "))

    if age in range(4):
        my_class = "유아"
    elif age in range(4,14):
        my_class = "어린이"
    elif age in range(14,19):
        my_class = "청소년"
    elif age in range(18,66):
        my_class = "성인"
    else:
        my_class = "노인"
    print("귀하의 등급은 %s이며 요금은 %d원 입니다." %(my_class,charge[my_class]))

    if charge[my_class]==0:
        print("")
        continue

    payment_way = int(input("요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용 카드): "))

    if payment_way == 1:
        payment=int(input("요금을 입력하세요: "))

        if payment<charge[my_class]:
            print("%d원이 모자랍니다. 입력하신 %d원을 반환합니다.\n" %((charge[my_class]-payment),payment))
            continue
        elif payment == charge[my_class]:
            print("감사합니다. 티켓을 발행합니다.")
        else:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." %(payment-charge[my_class]))
    elif payment_way == 2:
        print("(결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인)")
        if age<60:
            print("%d원 결제되었습니다. 티켓을 발행합니다." %(charge[my_class]*0.9))
        else:
            print("%d원 결제되었습니다. 티켓을 발행합니다." %((charge[my_class]*0.9)*0.95))
    else:
        print("요금 유형이 선택되지 않아 처음으로 돌아갑니다.\n")
        continue

    turn += 1
    
    if turn%7==0 and free_ticket>=0:
        free_ticket -= 1
        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. (잔여 무료티켓 %d장)" %free_ticket)
    elif turn%4 ==0 and annual_member_coupon>=0:
        annual_member_coupon -= 1
        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. (잔여 할인티켓 %d장)" %annual_member_coupon)

    print("")