class Account:  # outer -> class
    # 은닉 멤버 변수
    __balance = 0  # 잔액
    __accName = None # 예금주
    __accNo = None # 계좌번호

    # 생성자 : 초기화
    def __init__(self, bal, name, no):
        self.__balance = bal  # 잔액 초기화
        self.__accName = name  # 예금주
        self.__accNo = no  # 계좌번호

    # 계좌정보 확인 : getter
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    # 입금하기 : setter
    def deposit(self, money):
        if money < 0:
            print('금액 확인')
            return  # 함수 종료(exit)

        self.__balance += money

    # 출금하기 : setter
    def withdraw(self, money):
        if self.balance < money:
            print('잔액 부족')
            return  # 함수 종료(exit)

        self.__balance -= money


# object 생성
acc = Account(1000, '홍길동', '125-152-4125-41') # 생성자

# object.member()
#acc.__balance # error
bal = acc.getBalance()
print('계좌정보 : ', bal) # 계좌정보 :  (1000, '홍길동', '125-152-4125-41')

# 10,000원 입금
acc.deposit(10000)
bal = acc.getBalance()
print('계좌정보 : ', bal)