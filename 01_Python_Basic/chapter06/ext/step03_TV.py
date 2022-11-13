'''
기본 생성자(묵시적 생성자)
  - 생성자를 생략하면 기본 생성자가 만들어진다. 
'''

class default_cost : 
    
    # 생성자 없음(기본 생성자)  
    '''   
    def __init__(self): # 객체만 생성 
        pass
    '''
    
    def data(self, x, y):
        self.x = x
        self.y = y
        
    def mul(self):
        return self.x * self.y
        
obj = default_cost() # 기본 생성자
obj.data(10, 20)
result = obj.mul()
print('mul =', result) # mul = 200


# class 정의
class TV :
    # 멤버 변수(자료=명사) 
    channel = 10 # 10번 
    volume = 5 # 초기값 
    power = False # off/on(True)
    color = None   
    
    # 기본 생성자 : 객체만 생성 
    def __init__(self):
        pass
    
    # 멤버 함수(기능=동사) 
    def volumeUp(self):
        self.volume += 1
        
    def volumeDown(self):
        self.volume -= 1
        
    def changeColor(self, color):
        self.color = color
    
    def changePower(self):
        self.power = not(self.power) # 반전(F->T->F)
        
    def channelUp(self):
        self.channel += 1 
        
    def channelDown(self):
        self.channel -= 1
        
    def display(self): # tv 정보 출력 
        print('색상은 {0}, 전원 상태 : {1}, 채널 번호 : {2}'.
              format(self.color, self.power, self.channel))
    
    def display2(self): # tv 정보 출력 
        print('색상은 {0}, 전원 상태 : {1}, 채널 번호 : {2}, 볼륨 : {3}'.
              format(self.color, self.power, self.channel, self.volume))
            
tv1 = TV() # 생성자 = class()
tv1.display() # 색상은 None, 전원 상태 : False, 채널 번호 : 10

tv1.changeColor("파랑색")
tv1.changePower() # True
tv1.channelUp() # +1
tv1.display()
# 색상은 파랑색, 전원 상태 : True, 채널 번호 : 11


'''
문) tv2 객체를 다음과 같이 생성하시오.
 조건1> 전원 on
 조건2> 채널 : 18번 
 조건3> 색생 : 검정
 조건4> 객체 정보 출력 : display() 
'''

tv2 = TV() # 기본 생성자 

# 멤버 호출 
tv2.changePower()
for i in range(8) :
    tv2.channelUp() # 8회 호출 
tv2.changeColor("검정")

tv2.display()
# 색상은 검정, 전원 상태 : True, 채널 번호 : 18
    
'''
문2) TV 클래스에 volume 멤버를 추가하시오.
  조건1> 멤버 변수 : volume
  조건2> 멤버 함수 : volumeUp()/volumeDown()
  조건3> tv 객체 생성 후 tv 정보 출력 
'''        

tv3 = TV()    

tv3.changeColor("파랑색")
tv3.changePower()
tv3.channelDown() # 9
tv3.volumeUp() # 6
tv3.display2() # volume 멤버 포함     
# 색상은 파랑색, 전원 상태 : True, 채널 번호 : 9, 볼륨 : 6        
        
        
        
        
    














 