'''
평균, 분산, 표준편차 함수를 갖는 클래스 정의
'''
from math import sqrt

class Var_Sd :
    x = None # 변량 x - 전역변수 
    
    def __init__(self, x): # 생성자  
        self.x = x  # 초기화 
         
    def Mean(self): # 평균 계산 
        avg = sum(self.x) / len(self.x) # 멤버변수 등록 
        return avg        

    def Var(self): # 분산 계산
        avg = self.Mean()  # 호출 
        diff = [ (v - avg)**2   for v in self.x ]
        var = sum(diff) / ( len(self.x) - 1 ) # 합계 / (n-1)
        return var
        
    def Sd(self): # 표준편차 계산 
        sd =  sqrt(self.Var()) # 호출 
        return sd

'''
x = [5, 9, 1, 7, 4, 6]
var_sd = Var_Sd(x) # 기본 생성자 객체 생성 
print('평균 : ', var_sd.Mean())
print('분산 : ', var_sd.Var())
print('표준편차 : ', var_sd.Sd())
'''
   
'''
평균 :  5.333333333333333
분산 :  7.466666666666666
표준편차 :  2.7325202042558927
'''

