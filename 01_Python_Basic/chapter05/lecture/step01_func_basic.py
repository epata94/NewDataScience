'''
함수(Function)
 - 특정 1개 기능을 정의
 - 내장함수, 사용자 정의 함수 
 
 1. 내장함수 : built-in or import
    - built-in : 함수()
    - import : 모듈.함수()
    
2. 사용자 정의 함수 
형식) 
def 함수([인수]) :
    실행문
    실행문
    [return 값] 
'''

import builtins
dir(builtins) # 내장 클래스, 내장 함수 목록 보기
'''
# 내장 클래스
ArithmeticError
ZeroDivisionError

내장 함수/클래스 
'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'execfile', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'runfile', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
'''


dataset = list(range(1,6))
print(dataset) # [1, 2, 3, 4, 5]

# (1) builtins 함수
print('len=', len(dataset))
print('sum=', sum(dataset)) # sum= 15
print('max=', max(dataset))
print('min=', min(dataset))

# (2) import 함수
import statistics # 수학/통계 함수 모듈(statistics.py) - 방법1
from statistics import variance, stdev # - 방법2

# import
print('평균=', statistics.mean(dataset)) # 방법2
print('중위수=', statistics.median(dataset))
print("표본 분산=", variance(dataset))
print("표본 표준편차=", stdev(dataset))

# 모듈제공 함수 보기 
print(dir(statistics)) # 'pstdev', 'pvariance', 'stdev', 'variance'

# 객체 멤버 보기 : object.member()
print(dir(dataset)) # 'insert', 'pop', 'remove', 'reverse', 'sort'
dataset.insert(0, 0)
print(dataset) # [0, 1, 2, 3, 4, 5]
dataset.pop(0)
print(dataset) # [1, 2, 3, 4, 5]

# 2. 사용자 정의 함수

# (1) 인수가 없는 함수
def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')

userFunc1() # 함수 호출

# (2) 인수가 있는 함수
def userFunc2(x, y):
    print('userFunc2')
    z = x + y
    print('z=', z)

userFunc2(10, 20)  # 함수 호출

# (3) return 있는 함수
def userFunc3(x, y):
    print('userFunc3')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y
    
    return tot, sub, mul, div

# 실인수 : 키보드 입력
x = int(input('x 입력 : '))
y = int(input('y 입력 : '))

t, s, m, d = userFunc3(x, y)
print('tot =', t)
print('sub =', s)
print('mul =', m)
print('div =', d)

'''
tot = 30
sub = -10
mul = 200
div = 0.5
'''








