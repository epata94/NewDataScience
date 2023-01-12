import pandas as pd
from statsmodels.formula.api import ols,glm
import operator
from itertools import combinations

wine_file = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine_file.columns = wine_file.columns.str.replace(' ','_')

column_list = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide',
               'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']
answer_dict = {}

for column_idx in range(1, len(column_list)+1) :
    com_list = list(map(','.join, combinations(column_list, column_idx)))
    for com_list_len in range(len(com_list)) :
        exe_list = com_list[com_list_len].split(',')
        my_formula = 'quality ~ '

        for exe_list_len in range(len(exe_list)) :
            if exe_list_len != len(exe_list)-1 :
                my_formula = my_formula + exe_list[exe_list_len] + "+"
            else :
                my_formula = my_formula + exe_list[exe_list_len]

        lm = ols(my_formula, data=wine_file).fit()

        lm.summary()
        print("="*80)
        print("관찰 계수: %s, 유효 데이터: %s" %(dir(lm),len(lm.fittedvalues)))
        print("회귀 상관도: %s" %lm.rsquared_adj)
        print("고정 변수 별 회귀 계수:\n %s" %lm.params)
        indepen_var = wine_file[exe_list]
        new_observe = wine_file.loc[wine_file.index, indepen_var.columns]
        predicted_value = lm.predict(new_observe)
        predicted_value_rounded = [round(score) for score in predicted_value]

        count = 0
        for wine_idx in range(len(wine_file.index)) :
            if wine_file['quality'][wine_idx] == predicted_value_rounded[wine_idx] :
                count += 1
        answer_dict[(',').join(exe_list)] = count / len(wine_file) * 100

sortedAnswer = sorted(answer_dict.items(), key=operator.itemgetter(1), reverse=True)
print(sortedAnswer[0])