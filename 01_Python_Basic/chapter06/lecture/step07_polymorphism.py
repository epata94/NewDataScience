'''
다형성(polymorphism)
 - 여러 가지 형태를 가질 수 있는 능력
 - 한 가지 기능으로 2개 이상 결과 도출(+ -> 덧셈, 결합연산)
 - 상속관계에서만 나오는 용어
 - 하나의 참조변수로 여러 타입의 객체를 참조할 수 있는 것
   즉, 부모타입의 참조변수(t)로 자식타입의 객체를 다룰 수 있는 것이 다형성
 - 부모 객체 -> 특정 자식 멤버 호출
'''

# 다형성(polymorphism) 예


# (1) 부모 클래스
class Flight:

    # 부모 원형 함수
    def fly(self):
        print('날다, fly 원형 메서드')


# (2) 자식 클래스 : 비행기
class Airplane(Flight) :

    # 함수 재정의
    def fly(self):
        print('비행기가 날다.')

# (2) 자식 클래스 : 새
class Bird(Flight) :

    # 함수 재정의
    def fly(self):
        print('새가 날다.')

# (2) 자식 클래스 : 종이비행기
class PaperAirplane(Flight) :

    # 함수 재정의
    def fly(self):
        print('종이 비행기가 날다.')

# (3) 객체 생성
# 부모 객체 = 자식 객체(자식1, 자식2)
flight = Flight()  # 부모 클래스 객체
air = Airplane()  # 자식1 클래스 객체
bird = Bird()  # 자식2 클래스 객체
paper = PaperAirplane()  # 자식3 클래스 객체

# (4) 다형성
flight.fly() # 날다, fly 원형 메서드

flight = air
flight.fly() # 비행기가 날다.

flight = bird
flight.fly() # 새가 날다.

flight = paper
flight.fly() # 종이 비행기가 날다.

