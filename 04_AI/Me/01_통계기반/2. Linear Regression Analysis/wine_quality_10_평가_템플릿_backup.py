# 통계 모델:
# 목표 정답률:

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

print("결과 예측하기")
# wine = pd.read_csv(,sep=',',header=0)

match_dic={}
# 전체 독립변수 식별

# 최적의 독립변수 식별
# hint]
# combinations(,)
# lm = ols(, data=).fit()
# y_predicted = lm.predict()


# 정답률 최대값 찾기
# match_dic = sorted(, ,)
# print(match_dic)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d')
print("MAX 조합: %s >> %.2f %%")
