'''
클래스(class)?
 - 함수의 모임
 - 역할 : 다수의 함수와 공유 자료를 묶어서 객체 생성
 - 구성 : 멤버(member) + 생성자 
 - 멤버 : 변수(자료) + 함수(기능) 
 - 유형 : 사용자 정의 클래스, 내장 클래스(python)
 - 형식)
 class 클래스 :
     멤버(member) : 변수, 함수 
     생성자 : 객체 생성 
'''

# (1) 함수와 클래스

# 함수 정의
def calc_func(a, b): # outer 
    # 자료(data)
    x = a # 10
    y = b # 20
    
    # inner
    def plus():
        p = x + y
        return p
    
    def minus():
        m = x - y
        return m

    return plus, minus

p, m = calc_func(10, 20)
print('plus =', p())
print('minus=', m())

# 클래스 정의
class calc_class :
    # 변수 선언
    x = y = 0
    
    # 생성자 : 객체 생성 + [멤버변수 초기화] 
    def __init__(self, a, b):
        print('~~객체 생성~~')
        self.x = a # 10
        self.y = b # 20
    
    # 멤버 함수(기능)
    def plus(self): # self : 멤버(변수+함수) 참조 객체 
        p = self.x + self.y
        '''
        p : 지역변수 
        self.x, self.y : 전역변수  
        '''
        return p 
    
    def minus(self):
        m = self.x - self.y
        return m
    
      
# class(1) -> object(n) 생성 
obj1 = calc_class(10, 20) # 생성자 -> 객체1  

# object.member()  
print('plus = ', obj1.plus()) # plus =  30
print('minus =', obj1.minus()) # minus = -10

obj2 = calc_class(100, 50) # 생성자 -> 객체2
print('plus = ', obj2.plus()) # plus =  150
print('minus =', obj2.minus()) # minus = 50

print(id(obj1), id(obj2)) # 9498096 9498000


# (2) 클래스 구성요소
class Car:
    # 멤버 변수
    cc = 0 # 엔진 cc
    door = 0 # 문짝 개수
    carType = None # null

    # 생성자
    def __init__(self, cc, door, carType):
        # 멤버 변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType # 승용차, SUV

    # 멤버 메소드
    def display(self):
        print("자동차는 %d cc이고, 문짝은 %d개, 타입은 %s 이다."
              % (self.cc, self.door, self.carType))


# object 생성
car1 = Car(2000, 4, "승용차")  # 객체 생성 + 초기화
# object.member()
car1.display()  # info(kind) -> display(kind)

car2 = Car(3000, 5, "SUV")
car2.display()


# (3) 내장 클래스
import  datetime
from datetime import date, time # from 모듈 import 내장 클래스

help(date)
'''
Help on class date in module datetime:
class date(builtins.object)
 |  date(year, month, day) --> date object
'''

today = date(2019, 10, 23) # 생성자 -> object
print(today) # 2019-10-23

# object.member : 변수
print(today.year) # 2019
print(today.month) # 10
print(today.day) # 23

# object.member() : 함수 
w = today.weekday() # Monday == 0 ... Sunday == 6
print('요일 정보 : ', w) # 요일 정보 :  0(월)~6(일)


help(time)
'''
Help on class time in module datetime:

class time(builtins.object)
 |  time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
'''

currTime = time(21,4,30)
'''
datetime.time(0, 0) ~ datetime.time(23, 59, 59, 999999)
'''
print(currTime) # 21:04:00

print(currTime.hour) # 21
print(currTime.minute) # 4
print(currTime.second) # 0

isoTime = currTime.isoformat() # HH:MM:SS
print(isoTime) # 21:04:00

