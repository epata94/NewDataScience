'''
4. 중첩함수(inner function)

형식)
def  outer_func(인수) :
    문장1

    def inner_func(인수) :
        문장2
        return 문장2

    return inner_func
'''


# 3) 중첩함수 예

# (1) 일급 함수
def a():  # outer
    print('a 함수')

    def b():  # inner
        print('b 함수')

    return b

b = a()  # 외부 함수 호출 - a 함수
b()  # 내부 함수 호출 - b 함수

# (2) 함수 클로저
'''
- outer 함수 역할 : 값 생성, inner함수 포함
- inner 함수 역할 : 값 대상 연산 수행(합계 -> 평균) 
'''

data = list(range(1, 101))


def outer_func(data):
    dataSet = data  # 값(1~100) 생성

    # inner
    def tot():
        tot_val = sum(dataSet)
        return tot_val

    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val

    return tot, avg  # inner 반환


# 외부함수 호출 : data 생성
tot, avg = outer_func(data)

# 내부함수 호출
tot_val = tot()
print('tot =', tot_val)

avg_val = avg(tot_val)
print('avg =', avg_val)
'''
tot = 5050
avg = 50.5
'''

'''
문) 중첩함수 문제 
 - outer 함수 : data 생성, inner 함수 포함 
 - inner 함수 : data 대상으로 avg -> var(avg_val) -> std(var_val)
'''
from statistics import mean  # 평균
from math import sqrt  # 제곱근

data = [4, 5, 3.5, 2.5, 6.3, 5.5]


def scattering_func(data):  # outer
    dataSet = data  # data 생성

    # inner
    def avg_func():
        avg_val = mean(dataSet)
        return avg_val

    def var_func(avg):
        # var = (sum(변량-산술평균)**2)) / (n-1)
        diff = [ (data - avg) ** 2 for data in dataSet ]
        #print(diff)  # 1차원
        #print(sum(diff))  # 0차원
        var_val = sum(diff) / (len(dataSet) - 1)

        return var_val

    def std_func(var):
        std_val = sqrt(var)
        return std_val

    return avg_func, var_func, std_func  # inner 반환


# outer 호출
avg, var, std = scattering_func(data)

# 내부 함수 호출
print('평균 : ', avg())
print('분산 : ', var(avg()))
print('표준편차 :', std(var(avg())))
'''
평균 :  4.466666666666667
분산 :  1.9466666666666668
표준편차 : 1.39522996909709
'''

# 3) 획득자와 지정저, nonlocal : inner -> outer 변수 수정

'''
getter() : 함수 내 변수를 외부로 반환 함수 
setter() : 함수 내 변수를 외부에서 수정 함수 
'''


def main_func(num):
    num_val = num  # 함수 내 변수=100 -> 200

    def getter():  # 인수 없음, return 있음
        return num_val

    def setter(value):  # 인수 있음, return 없음
        nonlocal num_val  # outer 변수 지정
        num_val = value

    return getter, setter


getter, setter = main_func(100)  # num 생성

print('num =', getter())  # num = 100
setter(200)  # num 값 수정
print('num =', getter())  # num 수정 확인 : num = 200


# 4) 함수 장식자

# 래퍼 함수
def wrap(func) :
    def decorated() :
        print('방가워요!')
        func()
        print('잘가요!')
    return decorated # 클로저 함수

# 함수 장식자 적용
@wrap
def hello() :
    print('hi ~ ', "홍길동")


# 함수 호출
hello()
