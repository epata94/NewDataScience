'''
제어문(조건문) 
 - 조건문(if), 반복문(for, while) 
'''

'''
형식1)
if 조건식 :
    실행문1 
else :
    실행문2
'''
num = int(input('점수 입력(1~100) : '))
print('num = ', num)

if num % 2 != 0 :
    print('홀수')
else :
    print('짝수')
    
# system 날짜/시간 모듈(*.py) 
import datetime

today = datetime.datetime.now() # package.module.function()
print(today) # 2019-04-16 11:59:03.720903
print(type(today)) # <class 'datetime.datetime'>

day = today.weekday()
print(day) # 0~6(1)

if day >= 5 :
    print('주말')
else :
    print('평일')

'''
형식2
if 조건식1 :
    실행문1
elif 조건식2 :
    실행문2
elif 조건식3 :
    실행문3
else :
    실행문4
'''    

# 문) num 변수 대상 -> 등급 계산(A:100~90,B:89~80,C:79~70,D:69~60,F:60미만 학점)
# 출력 형식 => 점수 : 85, 등급 : B

grade = "" # 공백 
if num >= 90 :
    grade = "A"
elif num >= 80 :
    grade = "B"
elif num >= 70 :
    grade = "C"
elif num >= 60 :
    grade = "D"
else :
    grade = "F"

print(f"점수 : {num}, 등급 : {grade}")
print("점수 : %d, 등급 : %s"%(num, grade))

# 3항 연산자 
if num >= 60 :
    grade ="합격"
else : 
    grade ="불합격"
    
# 형식) 변수 =  참 if 조건식  else 거짓
grade =  "합격"  if num >= 60 else "불합격"
print('3항 연산자 : ', grade) # 3항 연산자 :  합격
    
# if 조건식 in 열거형data : 
s = input("문자열 입력 : ")

# 단어 검색 
if '홍길동' in s :
    print('\'홍길동\' 단어 있음')
else :
    print('\'홍길동\' 단어 없음')
    

# exam01



















