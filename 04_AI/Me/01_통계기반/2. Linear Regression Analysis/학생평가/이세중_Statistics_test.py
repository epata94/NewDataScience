import pandas as pd
from statsmodels.formula.api import ols, glm
from itertools import combinations

wine = pd.read_csv('winequality-both.csv',sep=',', header = 0)
wine.columns = wine.columns.str.replace(' ','_')
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density +fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'

lm = ols(my_formula, data = wine).fit()
print(lm.summary()) # 유의수준을 만족하지 못하는 두 변수를 제외하고 조합을 생성한다.
ind_list = ['alcohol', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH','residual_sugar','sulphates','total_sulfur_dioxide', 'volatile_acidity']

for a in range(0,9):
    k = list(combinations(ind_list, a))
    dependent_variable = wine['quality']
    for b in k:
        c = list(b)
        c.append("quality")
        independent_variables = wine[wine.columns.difference(c)]
        new_observations = wine.ix[wine.index.isin(range(10)), independent_variables.columns]
        y_predicted = lm.predict(new_observations)
        y_predicted_rounded = [round(score, 2) for score in y_predicted]
        print(y_predicted_rounded)
