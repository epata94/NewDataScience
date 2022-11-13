'''
예외처리 : run time error 발생 시 처리 
 - file/DB 입출력 시 사용 

try :
    예외발생 코드 
except 예외처리클래스 as 변수: 
    예외처리 코드 
finally :
    항상 실행 코드
'''

# 3. 예외 처리 활용 : 반복 수행 과정에서 예외처리 

'''
날짜별로 10 page 뉴스 crawling
  - 10 page가 안되는 경우 null로 인해서 예외 발생  
'''

# (1) 예외 발생 코드
print('프로그램 시작 !!!')
x = [10, 30, 25.2,'num', 14, 51]

for i in x :
    print(i)    
    y = i**2  # 예외 발생 type(s) for ** or pow(): 'str' and 'int'
    print('y =', y)

print('프로그램 종료')

# (2) 예외 처리 코드
print('프로그램 시작 !!!')
for i in x :
    try :            
        y = i**2  # 예외 발생 type(s) for ** or pow(): 'str' and 'int'
        print('i=', i, ', y =', y)
    except :  # except  Exception as e :
        print('숫자 아님 : ', i)
    
print('프로그램 종료')

import builtins
print(dir(builtins))

# 유형별 예외처리 
print('\n유형별 예외처리 ')
try :
    div = 1000 / 2.53
    print('div = %5.2f' %(div))  # 정상   
    #div = 1000 / 0                  # 1차 - 산술적 예외
    f = open('c:\\test.txt')         # 2차 - 파일 열기
    num = int(input('숫자 입력 : ')) # 3차 - 기타 예외 
    print('num =', num)
# 다중 예외처리 클래스
except Exception as e:
    print('오류 정보 :', e) # 오류 정보 : division by zero
except FileNotFoundError as e:
    print('오류 정보 : ', e) 
except Exception as e : # 기타 예외 처리
    print('오류 정보 : ', e)
    '''
    오류 정보 :  invalid literal for int() with base 10: 'test'
    10진수로 유효하지 않은 문자 
    '''
finally :
    print('finally 영역 - 항상 실행되는 영역')