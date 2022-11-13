'''
method :
 - class에서 정의한 함수 
 - method 유형 
 1. instance method : object.method() 호출, (self) 기본 인수 
 2. class method : class.method() 호출, (cls) 기본 인수 
'''

class DatePro :
    # 멤버 변수
    content = "날짜 처리 클래스"

    # 생성자
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    # 객체 메서드(instance method)
    def display(self):
        print("%d-%d-%d"%(self.year, self.month, self.day))
        
    # 클래스 메서드(class method)
    @classmethod # 함수 장식자 
    def date_string(cls, dateStr): # '19951025'
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]
        
        print(f"{year}년 {month}월 {day}일") # 1995년 10월 25일
        
# 객체 멤버
date = DatePro(1995, 10, 25) #  생성자
print(date.content) # 날짜 처리 클래스
print(date.year) # 1995
date.display() # 1995-10-25

# 클래스 멤버
print(DatePro.content) # 날짜 처리 클래스
#print(DatePro.year) # AttributeError
DatePro.date_string('19951025') # 1995년 10월 25일