def is_odd(num):
    if num%2==0:
        return "짝수"
    else:
        return "홀수"

num=6
print(f"주어진 수 = {num}")
print(f"검증 결과 = {is_odd(num)}")