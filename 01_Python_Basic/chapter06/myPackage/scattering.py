'''
- 산포도(Scatter)
   평균을 중심으로 자료들이 얼마나 흩어져 있는지의 정도를 나타내는 통계학 용어이다.
   산포도 값이 클 수록 많이 흩어져 있고, 반대로 산포도 값이 작으면 자료들의 분포가
   평균을 중심으로 고루 분포되었다는 의미이다.
   산포도의 통계는 분산(variance), 표준편차(standard deviation) 많이 이용한다.
   다음은 표본(sample)에 대한 분산과 표준편차의 수식이다.

   분산 = sum( (변량-산술평균)^2 ) / (n-1)
   표준편차 = sqrt(분산)
'''

from statistics import mean
from math import sqrt


# 산술평균 함수
def Avg(data):
    avg = mean(data)
    return avg


# 분산/표준편차 함수
def var_sd(data):  # [2,4,5,6,1,8] - avg
    avg = Avg(data)  # 함수 호출
    # list 내포
    diff = [(d - avg) ** 2 for d in data]

    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)

    return var, sd

data = [1, 3, 5, 7]
print('평균=', Avg(data))
var, sd = var_sd(data)
print('분산=', var)
print('표준편차=', sd)

# 프로그램 시작점
#if __name__ == "__main__" :

