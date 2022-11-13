'''
클래스 상속( Inheritance )
 - 기존 클래스를 이용하여 새로운 클래스 생성 문법 
 - 부모클래스 -> 자식클래스
 - 상속 대상 : 멤버(변수+함수)
 - 생성자는 상속 대상이 아님  
 
 형식)
 class new_class(old_class) :
     멤버 변수
     생성자
     멤버 함수
     
self vs super()
 - self : 현재 클래스의 멤버 호출 
 - super() : 부모 클래스의 멤버 호출  
'''

# 부모 클래스 
class Super :

    # 생성자 : 동적멤버 생성
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    # 멤버 함수 
    def display(self):
        print('name : %s, age : %d'%(self.name, self.age))

sup = Super('부모', 55)
sup.display() # 부모 멤버 호출         

#  자식 클래스
class Sub(Super) : # 클래스 상속
    gender = None # 자식 멤버
       
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender
        
    # 메서드 확장
    def display(self):
        print('name : %s, age : %d, gender : %s'
              %(self.name, self.age, self.gender))
    
sub = Sub('자식', 25, '여자')
sub.display() # 자식 멤버 호출 
# name : 자식, age : 25, gender : 여자            
        
# 2. super()

# (1) 부모클래스 정의
class Parent :

    # 생성자 : 객체 + 초기화 
    def __init__(self, name, job):
        self.name = name
        self.job = job
        
    # 멤버 함수(method)
    def display(self):
        print('name : {}, job : {}'.format(self.name, self.job))

# 부모 클래스 객체 생성
p = Parent('홍길동', '회사원')
p.display()
        
        
# (2) 자식 클래스 생성
class Children(Parent): # Parent(member) -> Childen1(member)
    gender = None # 추가 멤버
    
    # 생성자
    def __init__(self, name, job, gender):
        # 부모 생성자 호출 
        super().__init__(name, job) # name, job 초기화
        self.gender = gender # 자식 멤버

    # 멤버 함수(method) 
    def display(self): # 함수 재정의
        print('name : {}, job : {}, gender : {}'
              .format(self.name, self.job, self.gender))

# 자식 클래스 객체 생성
chil = Children("이순신", "해군 장군", "남자")
chil.display()



# 3. 자식 클래스2
'''
<조건1> 자식클래스명 : Childen2, 부모클래스 : Parent
<조건2> 자식클래스 멤버
   1) 부모클래스 멤버 상속 : name, job, display()
   2) 자식클래스 멤버 추가 : gender 추가 
   3) 자식클래스 멤버 초기화 : 부모멤버 -> 부모 생성자 호출 
   4) display() 재정의 -> 객체 결과 출력
'''
class Childen2(Parent):
    gender = None
    
    def __init__(self, name, job, gender):
        super().__init__(name, job)
        self.gender = gender
    
    # 함수 재정의     
    def display(self): # 함수 재정의 
        print('name : {}, job : {}, gender : {}'
              .format(self.name, self.job, self.gender))  
    
ch2 = Childen2("유관순", "독립열사", "여자")
ch2.display()    
    
    
    
    
    
    

        
        
        
        
