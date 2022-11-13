'''
중첩함수 -> Class 
  outer -> class
  outer 변수 -> 멤버 변수 
  inner -> 멤버 함수 
'''

class Account : # outer -> class
    
    balance = 0 # 멤버 변수 : 잔액 
    
    # 생성자 
    def __init__(self, bal, name, no):
        self.balance = bal # 잔액 초기화 
        self.accName = name # 예금주 
        self.accNo = no # 계좌번호 
    
    # 계좌정보 확인 : getter
    def getBalance(self): 
        return self.balance, self.accName, self.accNo
    
    # 입금하기 : setter
    def deposit(self, money):
        if money < 0 :
            print('금액 확인')
            return # 함수 종료(exit)
        
        self.balance += money
    
    # 출금하기 : setter 
    def withdraw(self, money):
        if self.balance < money :
            print('잔액 부족')
            return # 함수 종료(exit) 
        
        self.balance -= money
    
    
# object 생성 
acc1 = Account(1000, '홍길동', '125-152-4125-41') # 생성자 

# object.member()
bal = acc1.getBalance()
print('계좌정보 : ', bal) # (1000, '홍길동', '125-152-4125-41')

# 10,000원 입금 
acc1.deposit(-1000)
acc1.deposit(10000)
bal = acc1.getBalance()
print('계좌정보 : ', bal)

# 20000원 출금
acc1.withdraw(20000)
acc1.withdraw(5000) # 정상 출금 
bal = acc1.getBalance()
print('계좌정보 : ', bal)
 

'''
소유자(accName), 계좌번호(accNo) 동적 멤버 변수 추가하기 
'''










    
    
    
    
    