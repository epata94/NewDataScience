'''
반복문(while)

형식)
while 조건식 :
    반복문
    반복문 

loop : 반복문 집합    
'''

# 카운터(index)/누적변수 
idx = tot = 0

while idx < 5 : # 0 < 5    # True : loop(명령문 집합)- 수행
    idx += 1 # 카운터 변수
    tot += idx # 누적변수 : tot = tot + idx 
    print(idx, tot)

print(idx, tot) # 5 10

# 1 ~ 100 까지 3의 배수 합과 원소 추출하기
cnt = tot = 0
dataset = []  # 빈 list

while cnt < 100:  # 100회 반복
    cnt += 1  # 카운터

    if cnt % 3 == 0:
        tot += cnt  # 누적변수
        dataset.append(cnt)  # 3차 작성

print('1 ~ 100사이 3의 배수 합 = %d' % tot)  # 1683
print('dataset =', dataset)  # [3, 6, 9, ... 99]

# 문1) 1~100 사이에서 5의 배수이면서(and) 3의 배수가 아닌 합 계산하기
i = tot = 0
dataset = []  # 빈list

while i < 100:
    i += 1
    if i % 5 == 0 and i % 3 != 0:
        dataset.append(i)
        print(i, end=' ')
        tot += i
print('tot = %d' % tot)  # tot = 867
print()
print('dataset :', dataset)

# 문2) -1, 3, -5, 7, -9 ~ 99 까지의 합을 구하시오.

# 부호 변경
i = 1;
sign = -1
print('sign=', i * sign)  # sign= -1

idx = tot = 0  # 값 위치, 합
loc = 1  # 수열 위치

while idx < 100:
    if idx % 2 != 0:  # 값 위치 홀수

        if loc % 2 != 0:  # 수열 홀수 위치
            tmp = idx * sign  # 부호 변경
            print(tmp, end=' ')  # -1 -5 -9 -13 -17
            tot += tmp  # 누적합
        else:  # 수열 짝수 위치
            tot += idx
        loc += 1  # 수열 위치 변경(홀수값 내에서 위치)

    idx += 1  # 값 위치 변경

print('\ntot = %d' % tot)  # tot = 50


# 무한 loop : exit 조건식 포함
numData = []
 
while True :
    num = int(input("숫자 입력 : "))
    
    if num % 10 == 0 : # exit 조건식 
        print("프로그램 종료")
        break 
    else :
        print(num)
        numData.append(num)
        
print(numData)

#  random module 추가
import random #
help(random) # FUNCTIONS 참고

# random모듈 지원 함수
help(random.choice) # Choose a random element from a non-empty sequence.
help(random.randint) # Return random integer in range [a, b] - a ~ b 난수 정수 반환
help(random.random) # x in the interval [0, 1) - 0~1 난수 실수 반환
help(random.sample) # Chooses k unique random elements from a population sequence or set.
help(random.uniform) # Get a random number in the range [a, b) or [a, b] depending on rounding.
help(random.normalvariate) # random.normalvariate(mu=,sigma=)

# random 모듈은 컴퓨터에서 의해서 임의 난수를 발생시키는 함수들을 제공한다.
# 예를 들면 모집단으로 부터 임의 값을 추출하는 샘플링 작업이나 돈전을 던져서
# 앞면이 나올 확률을 구하기 위해서 컴퓨터로 시뮬레이션하는 경우 들 수 있다.
# random 모듈에서 제공되는 주요 함수와 기능은 다음 표와 같다.


# 0~1 사이 난수 실수
help(random.seed)
random.seed(123)
r = random.random()
print('r=', r)  # r= 0.3940

# [실습] 난수 0.01 미만이면 종료 후 난수 갯수 출력
cnt = 0
while True:
    r = random.random()
    print(random.random())
    if r < 0.01:
        break
    else:
        cnt += 1

print('난수 개수 = ', cnt)


help(random.randint)
help(random.choices)
# Help on method choices in module random:
# choices(population, weights=None, *, cum_weights=None, k=1) method of random.Random instance
#    Return a k sized list of population elements chosen with replacement.
# 모집단 요소의 k 크기 목록을 반환합니다

# 이름 list
names = ['홍길동', '이순신', '유관순']
print(names)  # 전체 이름, 특정 이름 출력
print(names[2])

if '유관순' in names:
    print('유관순 있음')
else:
    print('유관순 없음')

# 이름 선택 : 0~2 난수 정수
print('random.randint')
idx = random.randint(0, 2)
print(names[idx])  # 이순신


print('random.choices')
name = random.choices(names, k=2)
print(name)  # ['이순신', '홍길동'] -> random 선택


'''
continue, break
 - continue : 계속 반복, 다음 문장 skip
 - break : 탈출(exit)
'''

i = 0
while i < 10:
    i += 1  # 카운터
    if i == 3:
        continue  # 1 2 4 5 6 7 8 9 10 -> 다음 문장 skip
    if i == 6:  # 2차 작성
        break  # 1 2 4 5  -> exit
    print(i, end=' ')
