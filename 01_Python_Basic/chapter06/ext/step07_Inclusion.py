'''
1. private 변수 = 은닉변수 
   object.member : x
   getter/setter 이용 : 은닉변수 참조 

2. class 포함관계(inclusion)
  - 특정 객체가 다른 객체를 포함하는 클래스 설계 기법 
  - 두 객체 간의 통신 지원 
  - ex) A(a) <-> B(b)
'''

# Login(uid, pwd)

class Login :
    
    # 생성자 
    def __init__(self, uid, pwd):
        # private 변수 : self.__변수 
        self.__uid = uid
        self.__pwd = pwd
    
    # getter : 반환 함수 
    def getInfo(self):
        return self.__uid, self.__pwd
        
    # setter : 수정 함수
    def setInfo(self, uid, pwd):
        self.__uid = uid
        self.__pwd = pwd
    
login = Login('hong', '1234')
# object.member
#print(login.__uid) # error

# getter 호출 : 은닉변수 확인 
uid, pwd = login.getInfo()
print(uid, pwd) # hong 1234

# setter 호출 : 은닉변수 수정 
login.setInfo('lee', '4567')

uid, pwd = login.getInfo()
print(uid, pwd) # lee 4567


# Server
class Server :
    # 멤버 변수 
    obj = None # obj = login
    uid = pwd = None # login('lee', '4567') -> uid='lee', pwd = '4567'
    
    # 멤버 함수 
    def send(self, obj):
        self.obj = obj
    
# A : Login <-> B : Server  

# A 객체  
login = Login('hong', '1234') 

# B 객체 
server = Server() # 기본생성자 -> 객체 
server.send(login)

# 1) B객체 -> A객체(getter)
uid, pwd = server.obj.getInfo()
print('id : ', uid)
print('pwd : ', pwd)
'''
id :  hong
pwd :  1234
'''

# 2) B객체 -> A객체(setter)
server.obj.setInfo('lee', '4567')
uid, pwd = server.obj.getInfo()
print('id : ', uid)
print('pwd : ', pwd)
'''
id :  lee
pwd :  4567
'''

# 3) B객체 -> A객체(uid/pwd) -> B객체(uid/pwd)
uid, pwd = server.obj.getInfo()

server.uid = uid # id 할당 
server.pwd = pwd # pwd 할당

print('server id :', server.uid) 
print('server pwd :', server.pwd)
'''
server id : lee
server pwd : 4567
'''





