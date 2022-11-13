'''
연산자(operator) 
1. 산술연산자
2. 관계연산자
3. 논리연산자
4. 대입연산자
5. print 출력 양식
6. 키보드 입력, 형 변환(Casting)
'''

# 1. 산술연산자
num1 = 100 # 피연산자1
num2 = 20  # 피연산자2

add = num1 + num2 # 덧셈
print('add=', add)

sub = num1 - num2 # 뺄셈
print('sub=', sub) # 80

mul = num1 * num2 # 곱셈
print('mul=', mul)

div = num1 / num2 # 나눗셈
print('div=', div)

div2 = num1 % num2 # 나머지 계산
print('div2=', div2) # 0

square = num1**2 # 제곱 계산(num1 ** 2)
print('square=', square) # 10000


#2. 관계연산자 예문
# (1) 동등비교
bool_result = num1 == num2 # 두 변수의 값이 같은지 비교
print(bool_result)
bool_result = num1 != num2 # 두 변수의 값이 다른지 비교
print(bool_result)

# (2) 크기비교
bool_result = num1 > num2 # num1값이 큰지 비교
print(bool_result)
bool_result = num1 >= num2 # num1값이 크거나 같은지 비교
print(bool_result)
bool_result = num1 < num2 # num2 이 큰지 비교
print(bool_result)
bool_result = num1 <= num2 # num2 이 크거나 같은지 비교
print(bool_result)

# 3. 논리연산자 예문
log_result = num1 >= 50 and num2 <=10 # 두 관계식이 같은지 판단
print(log_result) # FALSE
log_result = num1 >= 50 or num2 <=10 # 두 관계식 중 하나라도 같은지 판단
print(log_result)

log_result = num1 >= 50 # 관계식 판단
print(log_result)
log_result = not(num1 >= 50) # 괄호 안의 관계식 판단 결과에 대한 부정
print(log_result)

# 4. 할당 연산자
# 1) 변수에 값 할당(=)
i = tot = 10 # sum - 경고
i += 1
tot += i 
print(i, tot)

# 같은 줄에 중복 출력 
print('출력1', end=' , ') # end='구분자'
print('출력2')

v1, v2 = 100, 200
print(v1, v2) # 100 200

# 2) 변수 교체
v2, v1 = v1, v2
#print(v1, v2) # 200 100

# 3) 패킹(packing) 할당
lst = [1,2,3,4,5]
v1, *v2 = lst
print(v1, v2) # 1 [2, 3, 4, 5]

*v1, v2 = lst
print(v1, v2) # [1, 2, 3, 4] 5

*v1, v2, v3 = lst
print(v1, v2, v3) # [1, 2, 3] 4 5


# 2. print 출력 양식

# 1) format(value, '양식')
print( format(3.14159, '8.3f') ) #    3.142
print('원주율 = ', format(3.14159, '8.3f'))

print( format(12345, '10d')) #      12345
print( format(12345, '3,d')) # 12,345

# 함수 도움말 보기 
#help(format)
# Help on built-in function format in module builtins: 내장함수 
#help('FORMATTING') # format 설명서 

# 2) 양식문자와 값 표현   
# 형식) print( '%양식문자' %(값) )

'''
%양식문자
%s : 문자열
%c : 한개 문자 
%d : 정수 
%f : 실수 
%o : 8진수
%x : 16진수 
%% : % 출력
'''

num1 = 10; num2 = 20
tot = num1 + num2
print('10 + 20 = %d' %tot ) # 10 + 20 = 30
print('%d + %d = %d' %(num1, num2, tot) ) # 10 + 20 = 30
print('이름은 %s 이고, 나이는 %d 입니다.' %('홍길동', 35))
# 이름은 홍길동 이고, 나이는 35 입니다.

print('전체 %d%%가 170cm 이상이다.' %50)
# 전체 50%가 170cm 이상이다.

# 3) 외부 상수 받기 
# 형식) print( '{ }' .format(값) )
print('이름은 {} 이고, 나이는 {} 입니다.' .format('홍길동', 35))
print('이름은 {1} 이고, 나이는 {0} 입니다.' .format(35, '홍길동'))

# 축약형 
name = "홍길동"; age = 35
print(f'이름은 {name} 이고, 나이는 {age} 입니다.')
# 이름은 홍길동 이고, 나이는 35 입니다.





# 카운터 변수/누적 변수
cnt = 0
cnt = cnt + 1 # 카운터 변수 
cnt += 1  # 카운터 변수
#cnt++ 
print(cnt) # 2

tot = 0
tot += cnt # 누적변수 : tot = tot(0) + cnt(2)
print(tot)

# 5. 키보드 입력, 형 변환(Casting)

# 키워드(문자열) -> 정수 
a = int(input('첫번째 숫자 입력 : ')) # 키보드 -> 정수 
b = int(input('두번째 숫자 입력 : ')) # 20
add = a + b
print('add = %d'%add)

# 키보드(문자열) -> 실수 
a = float(input('첫번째 숫자 입력 : ')) # 키보드 -> 실수 
b = float(input('두번째 숫자 입력 : ')) # 
add = a + b
print('add = %.3f'%add)

print(int(24.5)) # 24
#print(int('hello')) # ValueError
#print(int('two')) # ValueError
print(2 + int('2')) # 4

# boolean -> 정수 
print(int(True)) # 1
print(int(False)) # 0

