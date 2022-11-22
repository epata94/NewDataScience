# 리턴타입: X, 매개변수: X
def add_number():
    first_num = int(input("첫번째 수를 입력하세요: "))
    second_num = int(input("두번째 수를 입력하세요: "))

    result = first_num + second_num

    print(f'{first_num} + {second_num} = {result}')

add_number()

#######################################################
# 리턴타입: X, 매개변수: O
def add_number2(first_num, second_num):

    result = first_num + second_num

    print(f'{first_num} + {second_num} = {result}')


first_num = int(input("첫번째 수를 입력하세요: "))
second_num = int(input("두번째 수를 입력하세요: "))
add_number2(first_num, second_num)

#######################################################
# 리턴타입: O, 매개변수: X
def add_number3():
    first_num = int(input("첫번째 수를 입력하세요: "))
    second_num = int(input("두번째 수를 입력하세요: "))
    result = first_num + second_num

    print(f'{first_num} + {second_num} = ', end='')
    return result

print(add_number3())

#######################################################
# 리턴타입: O, 매개변수: O
# def add_number4(first_num, second_num):
#     result = first_num + second_num
#     return result

def add_number4(first, second):
    result = first + second
    return result

first_num = int(input("첫번째 수를 입력하세요: "))
second_num = int(input("두번째 수를 입력하세요: "))
print(f'{first_num} + {second_num} = {add_number4(first_num,second_num)}')
print(f'{first_num} + {second_num} = {add_number4(1,2)}')
print(f'{first_num} + {second_num} = {add_number4(second_num,first_num)}')
result = add_number4(2,3)
