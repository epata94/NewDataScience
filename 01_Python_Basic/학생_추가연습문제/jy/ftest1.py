#1.	두 수를 입력 받아 나누기를 수행하는 my_div(num1, num2) 함수를 작성한다. 리턴 값은 두수를 나눈 값, 몫, 나머지 이다. 분모가 0일 경우 예외처리를 한다.

def my_div(num1, num2):
    try:
        result = num1/num2
        share = num1//num2
        remainder = num1%num2

        return result, share, remainder

    except ZeroDivisionError as e:
        print("0으로 나눌 수 없습니다",e)


print(f"결과: {my_div(186,6)}")
