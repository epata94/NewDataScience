
def my_div (num1,num2):
    try:
        value = num1 / num2
        result = num1 // num2
        remainder = num1 % num2
    except Exception as e:
        print(f"예외 발생 : {e}")
    finally:
        return value,result,remainder


number = input("나누기를 할 두 수를 입력하세요 (예 4 2)")
#print(number)
num_list =[]
num_list = number.split()
#print(num_list)
num1 = int(num_list[0])
#print(num1)
num2 = int(num_list[1])
#print(num2)

result_list = my_div(num1,num2)
print("두 수를 나눈 값 :",format(result_list[0],"2.1f"))
print(f"두 수를 나눈 몫 : {result_list[1]}")
print(f"두 수를 나눈 나머지: {result_list[2]}")


