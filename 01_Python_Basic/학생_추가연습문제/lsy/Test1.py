def my_div(num1,num2):
    try:
       val=num1/num2
       share=int(num1/num2)
       rest=num1%num2

       return val, share,rest
    except Exception as e:
        print(f"ERROR: {e}")

num1, num2= map(int,input("두 수를 입력하시오 " ).split(' '))
val,share,rest=my_div(num1,num2)
print(f'값: {val} 몫: {share} 나머지: {rest}')