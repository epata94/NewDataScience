x = 50
def local_func(x):
    x += 50 # x = x+50
    print(f'지역변수 x: {x}')

def print_x():
    print(f'함수에서 전역변수 읽기 시도: {x}')
    x +=  50 # 함수에서 전역변수 변경 시도

local_func(x)
print(f'전역변수 x={x}')
print_x()
