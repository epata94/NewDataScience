import pandas as pd
import operator
from statsmodels.formula.api import ols, glm
from itertools import combinations

wine_csv = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine_csv.columns = wine_csv.columns.str.replace(' ', '_')
my_formula_for_ols = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
                     'pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm_for_summary = ols(my_formula_for_ols, data=wine_csv).fit()
print("lm.summary ")
print(lm_for_summary.summary())

columns_for_combinations = ['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide',
               'pH', 'residual_sugar', 'sulphates', 'total_sulfur_dioxide', 'volatile_acidity']
match_dictionary = {}

for number in range(1, 12):
    combination_list = list(combinations(columns_for_combinations, number))
    for tuple in combination_list:
        my_formula_for_max = 'quality ~ '
        for data in tuple:
            my_formula_for_max += '%s + ' % data
        my_formula_for_max = my_formula_for_max.strip().rstrip('+')
        lm = ols(my_formula_for_max, data=wine_csv).fit()
        dependent_var = wine_csv['quality']
        independent_vars = wine_csv[list(tuple)]
        predicted_var = lm.predict(independent_vars)
        predicted_var_rounded = [round(score) for score in predicted_var]
        match_count = 0
        for index in range(len(predicted_var_rounded)):
            if predicted_var_rounded[index] == dependent_var.values[index]:
                match_count += 1
        print("조합 : %s" % my_formula_for_max.replace('quality ~ ', ''))
        print("정답률 : %.2f %%" % (match_count / len(predicted_var_rounded)*100))
        match_dictionary['%s' % my_formula_for_max.replace('quality ~ ', '')] = match_count/len(predicted_var_rounded)*100

match_dictionary = sorted(match_dictionary.items(), key=operator.itemgetter(1), reverse=True)
print("\n최대값 조합 : %s, 정답률 : %.2f %%" % (match_dictionary[0][0], match_dictionary[0][1]))