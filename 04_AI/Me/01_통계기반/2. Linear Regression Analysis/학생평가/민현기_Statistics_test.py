import pandas as pd
from statsmodels.formula.api import ols, glm
from itertools import combinations
import operator

wine_data = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine_data.columns = wine_data.columns.str.replace(' ', '_')

formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
linear_lm = ols(formula, data=wine_data).fit()

# 회귀분석 요약정보 확인
print(linear_lm.summary())

# 예측
quality = list(wine_data.loc[:, 'quality'])
my_combination = 'quality ~ '
independent_col_list = ['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH', 'residual_sugar',
                        'sulphates', 'total_sulfur_dioxide', 'volatile_acidity']
my_dict = {}
print('\n 모든 변수 조합에 대한 회귀분석 중입니다.')
for i in range(1, len(independent_col_list)+1):
    comb = list(combinations(independent_col_list, i))
    for comb_tup in comb:
        comb_data = ' + '.join(list(comb_tup))
        my_variable = my_combination + comb_data
        my_lm = ols(my_variable, data=wine_data).fit()

        independent_col = wine_data[wine_data.columns.difference(['quality', 'type'])]
        observe_list = wine_data.loc[wine_data.index.isin(range(len(wine_data))), independent_col.columns]

        predict_value = my_lm.predict(observe_list)
        predict_value_round = [round(score) for score in predict_value]

        ok = 0
        for num in range(len(wine_data)):
            if predict_value_round[num] == quality[num]:
                ok += 1

        my_dict['%s'%my_variable] = round(ok/len(wine_data)*100, 2)


my_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)
print('\n정답률이 최대가 되는 조합 : %s \n정답률 : %s' %(my_dict[0][0], my_dict[0][1]))
