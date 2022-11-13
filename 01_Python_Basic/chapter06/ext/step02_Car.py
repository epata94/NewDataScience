'''
동적 멤버 변수 생성
  - 필요한 경우 특정 함수에서 멤버 변수 생성 
self : 자신의 멤버를 호출하는 객체 
  self.멤버변수 
  self.멤버함수()  
'''

class Car :
    # 멤버 변수 
    #door = cc = 0
    #name = None # null
    
    # 생성자 
    def __init__(self, name, door, cc):
        # 동적 멤버 변수 
        self.name = name
        self.door = door
        self.cc = cc
        
    # 멤버 함수
    def info(self):
        self.kind = "" # 동적 멤버 변수 
        if self.cc >= 3000 :
            self.kind = "대형"
        else :
            self.kind = "중소형" 
        # 멤버 함수 호출   
        self.display()  
           
            
    def display(self):             
        print("%s는 %d cc이고(%s), 문짝은 %d개 이다."
              %(self.name, self.cc, self.kind, self.door))
    
# object 생성 
car1 = Car("소나타", 4, 2000) # 객체 생성 + 초기화 
# object.member()
car1.info() #  info(kind) -> display(kind)
        
car2 = Car("그랜저", 4, 3000)
car2.info()        
        
        
        
        
        
        
        
        
         


