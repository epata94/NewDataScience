# 10 미만의 자연수에서 3과 5의 배수를 구하면
# 3, 5, 6, 9이다. 이들의 총합은 23이다.
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
def add_until(num,until):
    sum=0
    i=1
    while True:
        if(num*i >= until): break
        sum += num*i
        i+=1
    return sum

answer=add_until(3,1000)+add_until(5,1000)-add_until(3*5,1000)
print(answer)