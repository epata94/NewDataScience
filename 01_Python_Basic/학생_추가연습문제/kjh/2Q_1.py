def my_div(num1, num2):
    return num1 / num2, num1 // num2, num1 % num2

try:
    print(my_div(10, 0))

except Exception as e:
    print(e)

