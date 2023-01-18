# 통계 모델: 선형회귀 분석 (Linear Regression Analysis)

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations
from datetime import datetime
import time

start = datetime.fromtimestamp(time.time())
print("결과 예측하기")
house = pd.read_csv('Boston_house.csv',sep=',',header=0)
house.columns = house.columns.str.replace(' ','_')

match_dic={}
colums_list = ['AGE','B','RM','CRIM','DIS','INDUS','LSTAT',
               'NOX','PTRATIO','RAD','ZN','TAX','CHAS']

for num in range(1,len(colums_list)+1):
    combi_list = list(combinations(colums_list,num))
    for tup in combi_list:
        my_formula = 'Target ~ '
        for data in tup:
            my_formula+='%s + '%data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=house).fit()
        dependent_variable = house['Target']
        # independent_variables = house[house.columns.difference(['quality','type','in_sample'])]
        independent_variables = house[list(tup)] # formula 에 들어간 columns만 골라서 고정 변수로 줌
        y_predicted = lm.predict(independent_variables)

        # 선형회귀모델에서 정답률로 모델을 평가하기에는 제약사항이 많다.
        # 예측값의 범위가 클 수록 수치를 최말단 자리까지 예측하기 어렵기 때문이다.
        # 선형모델은 1차방정식에 기인한 예측모델이며 이는 평균에 수렴한다.
        # 따라서 평균에 근접하여 얼마나 차이가 적은지 마진을 주어야 한다.
        # 추후 머신러닝에는 선형회귀를 평가하는 적합한 방식을 제공한다.
        # 정답률로 평가하기 위해서는 예측값, 실제값을 자리수에 맞추어
        # 반올림, 올림, 내림등의 동일 방식으로 스케일을 조정할 필요가 있다.
        y_predicted_rounded = [round(score) for score in y_predicted]

        for index, score in enumerate(y_predicted_rounded):
            if len(str(score)) > 1:
                y_predicted_rounded[index] = round(score,-1)


        match_count=0
        for index in range(len(y_predicted_rounded)):
            target_price = 0
            if len(str(round(dependent_variable.values[index]))) == 1:
                target_price = round(dependent_variable.values[index])
            else:
                target_price = round(dependent_variable.values[index],-1)
            if y_predicted_rounded[index] == target_price:
                match_count+=1
        print('\n>> '+my_formula.replace('quality ~ ',''))
        print('>> match count=',match_count)
        print('>> 정답률: %.2f %%'%(match_count/len(y_predicted_rounded)*100))
        match_dic['%s'%my_formula.replace('quality ~ ','')] = match_count/len(y_predicted_rounded)*100


# 최대값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)
# print(match_dic)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d'%len(match_dic))
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0],match_dic[0][1]))
end = datetime.fromtimestamp(time.time())
print(f'분석 시작: {start}')
print(f'분석 종료: {end}')
print(f'총 분석 시간: {end-start}')