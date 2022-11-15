def print_max(num1,num2,num3):
    # global max
    max=0
    if max<num1:
        max=num1
    if max<num2:
        max=num2
    if max<num3:
        max=num3

    print(f"가장 큰 값 {max}")

num1,num2,num3=input("숫자 세개를 공백을 두고 입력 하여 주세요 : ").split()

print_max(int(num1),int(num2),int(num3))