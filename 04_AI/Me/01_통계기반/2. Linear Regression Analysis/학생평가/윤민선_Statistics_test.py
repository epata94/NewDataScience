import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

wine_data = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine_data.columns = wine_data.columns.str.replace(' ','_')

column_list = ['fixed_acidity','volatile_acidity','citric_acid','residual_sugar','chlorides',
               'free_sulfur_dioxide','total_sulfur_dioxide','density','pH','sulphates','alcohol']
dependent_value = wine_data['quality']
match_dictionary={}
for num in range(1,len(column_list)+1):
    combi_list = list(combinations(column_list,num))
    for tup in combi_list:
        formula = 'quality ~ '
        for data in tup:
            formula+='%s + '%data
        formula = formula.strip().rstrip('+')
        ols_model = ols(formula, data=wine_data).fit()
        print(ols_model.summary())
        independent_list = wine_data[list(tup)]
        predict_data = ols_model.predict(independent_list)
        predict_data_round = [round(p_data) for p_data in predict_data]
        match_count=0
        for index in range(len(predict_data_round)):
            if predict_data_round[index] == dependent_value[index]:
                match_count+=1
        key_formula = formula.replace('quality ~ ','')
        match_percent = match_count/len(predict_data_round)*100
        match_dictionary[key_formula] = match_percent
        print('\n>> %s'%key_formula)
        print('>> Match Count : %d'%match_count)
        print('>> 정답률: %.2f %%'%match_percent)

match_dictionary = sorted(match_dictionary.items(),key=operator.itemgetter(1),reverse=True)
print('\n>> 총 조합 갯수: %d'%len(match_dictionary))
print('>> MAX 조합 : %s'%match_dictionary[0][0])
print('>> MAX 정답률: %.2f %%'%match_dictionary[0][1])