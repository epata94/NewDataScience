'''
패키지(Package) = 폴더 
 - 유사한 모듈(python file)을 꾸러미로 묶어놓은 단위
모듈(Module) = 파일 
 - 함수와 클래스로 구성된 python file(*.py)
 형식) 
 - 패키지명.모듈.함수 
 - 패키지명.모듈.클래스 
'''



# 1. 모듈 추가 (방법1)
# 형식) import 패키지명.모듈명
import chapter06.myPackage.scattering

# 데이터 셋
data = [1, 3, 1.5, 2, 1, 3.2]

# 평균 함수 호출
print('평균 : ', chapter06.myPackage.scattering.Avg(data)) # 평균 :  1.95

# 분산과 표준편차 함수 호출
var, sd = chapter06.myPackage.scattering.var_sd(data)
print('분산 :', var) # 분산 : 0.9350000000000002
print('표준편차 :', sd) # 표준편차 : 0.9669539802906859


# 2. 모듈 추가 (방법2)
# 형식) from 패키지명.모듈명 import 함수명 
from chapter06.myPackage.scattering import Avg, var_sd# 함수 or 클래스

print('평균 : ', Avg(data)) # 평균 :  1.95

var, sd = var_sd(data) # 평균 :  1.95
print('분산 :', var) # 분산 : 0.9350000000000002
print('표준편차 :', sd) # 표준편차 : 0.9669539802906859



