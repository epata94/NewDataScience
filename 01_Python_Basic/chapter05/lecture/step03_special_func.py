'''
함수의 가변인수
 - 한 개 가인수로 여러 개 실인수 받을 수 있는 인수
 형식) def 함수명(*인수)
'''

# (1) 여러 명의 이름 받는 가변인수
def Func1(name, *names):
    print(name)  # 가인수 : 홍길동
    print(names)  # 가변 인수 : ('이순신', '유관순')


Func1("홍길동", "이순신", "유관순")

# statistics 모듈 import
from statistics import mean, variance, stdev

# (2) 통계량 구하는 함수
def statis(func, *data):
    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std':
        return stdev(data)  # var, sd
    else:
        return 'TypeError'

print('avg=', statis('avg', 1, 2, 3, 4, 5))  # sum= 15
print('var=', statis('var', 1, 2, 3, 4, 5))  # avg= 3
print('std=', statis('std', 1, 2, 3, 4, 5))  # var= (2.5, 1.5811388300841898)

'''
sum= 15
avg= 3
var= (2.5, 1.5811388300841898)
var= 2.5
'''

print('mean =', statis('mean', 1, 2, 3, 4, 5))  # mean = TypeError


# *인수 -> ():tuple
# **인수 -> {}:dict

# (3) 사전형 가변인수
def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)  # {'addre': '서울시', 'height': 175, 'weight': 65}


emp_func('홍길동', 35, addre='서울시', height=175, weight=65)

'''
2. 축약함수(Lambda)
 - 한 줄 함수
 형식) 변수 = lambda 인수 : 리턴값
 ex) lambda x,y : x+y

3. scope
  - 전역변수/지역변수
'''

# 2. 축약함수(Lambda)

# (1) 일반함수
def Adder(x, y):
    add = x + y
    return add

print('add=', Adder(10, 20))

# (2) 람다 함수
print('add=', (lambda x, y: x + y)(10, 20))



# lambda에서 가변 인수 사용
calc = lambda dan, su: dan * su
print('price =', calc(2500, 5))  # price = 12500

calc2 = lambda dan, *su, **product: print(dan, su, product)

calc2(10000, 3, 5, a=2500, b=3000)
# 10000 (3, 5) {'a': 2500, 'b': 3000}


# 3. scope : 전역변수/지역변수

# 전역변수 : 전 지역 사용
# 지역변수 : 함수 or 블럭(if, while, for) 사용

x = 50  # 전역변수


def local_func(x):
    x += 50  # 지역변수 -> 종료 시점 소멸


local_func(x)
print('x=', x)  # x= 50


def global_func():
    global x  # 전역변수 x 사용
    x += 50  # x+50 = 100


global_func()
print('x=', x)  # x= 100

data = [1, 3, 5, 7, 9]
tot = 0  # 전역변수


def calc_func(data):
    global tot  # tot=0
    for d in data:
        tot += d  # error  tot(null) = tot(null) + d(1)
    return tot


tot = calc_func(data)
print('tot=', tot)  # tot= 25


