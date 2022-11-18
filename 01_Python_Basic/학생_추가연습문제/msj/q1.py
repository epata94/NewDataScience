def my_div(num1, num2) :
    try:
        result = num1 / num2
        quotient = num1 // num2
        remainder = num1 % num2

        return result, quotient, remainder
    except Exception as e:
        print('예외 발생 : ', e)

print(my_div(2,3))