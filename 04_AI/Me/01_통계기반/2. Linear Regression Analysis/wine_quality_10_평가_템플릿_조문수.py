# 통계 모델:
# 목표 정답률:

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

print("결과 예측하기")
# wine = pd.read_csv(,sep=',',header=0)
# wine.columns = wine.columns.str.replace(' ','_')

match_dic={}
# 전체 독립변수 식별
colums_list = []

# 최적의 독립변수 식별
# combi_list = list(combinations(,))


# lm = ols(, data=).fit()
# despendent_variable =
# independent_variables =
# y_predicted = lm.predict()
# y_predicted_rounded = [round(score) for score in y_predicted]


# 정답률 최대값 찾기
# match_dic = sorted(match_dic.items(), key=operator.itemgetter(1), )
# print(match_dic)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d')
print("MAX 조합: %s >> %.2f %%")
