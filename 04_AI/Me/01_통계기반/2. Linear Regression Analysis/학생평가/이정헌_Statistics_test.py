import pandas as pd
from statsmodels.formula.api import ols, glm
import operator
from itertools import combinations

wine_qulity = pd.read_csv('winequality-both.csv',sep=',', header=0)
wine_qulity.columns = wine_qulity.columns.str.replace(' ', '_')


all_list=['fixed_acidity','volatile_acidity','citric_acid','residual_sugar','chlorides','free_sulfur_dioxide','total_sulfur_dioxide','density','pH','sulphates','alcohol']

all_list_formula='quality ~ fixed_acidity + volatile_acidity + citric_acid+residual_sugar+chlorides+free_sulfur_dioxide+total_sulfur_dioxide+density+pH+sulphates+alcohol'

allsds='quality~fixed acidity+volatile acidity+citric acid+residual sugar+chlorides+free sulfur dioxide+total sulfur dioxide+density+pH+sulphates+alcohol'


i = 0

lm = ols(all_list_formula, data=wine_qulity).fit()
print(lm.summary())
for line_num in range(1,len(all_list)):
    line_list=list(combinations(all_list,line_num))
    inter_list = []
    for sel_list in line_list:
        # print()
        # sel_list=','.join(list(sel_list))
        inter_list2=list(sel_list)

        inter_list='+'.join(inter_list2)
        b='quality~%s'%inter_list


        lm = ols(b, data=wine_qulity).fit()
        inde_va = wine_qulity[inter_list2]

        qulity_value=wine_qulity['quality']
        # print(qulity_value)

        y_predicted = lm.predict(inde_va)
        count=0
        y_round=[round(score) for score in y_predicted]

        for i in range(len(wine_qulity)):
            if qulity_value[i] == y_round[i]:
                count+=1

        print(inter_list)
        print('정답률%s%%'%(count/len(wine_qulity))*100)
        print('')




