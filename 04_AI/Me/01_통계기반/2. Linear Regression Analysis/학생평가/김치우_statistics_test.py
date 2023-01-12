import pandas as pd
from statsmodels.formula.api import ols,glm
import operator
from itertools import combinations

wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ', '_')

columns_list = 'fixed_acidity ~ quality + fixed_acidity + volatile acidity + citric acid + residual sugar + chlorides + free sulfur dioxide + total sulfur dioxide + density + pH + sulphates + alcohol + quality'
list = 'fixed_acidity + volatile acidity + citric acid + residual sugar + chlorides + free sulfur dioxide + total sulfur dioxide + density + pH + sulphates + alcohol + quality'

for list in list(combinations(columns_list,num)):

y_predicted = lm.predict(list)

lm = ols(my_formula, data=wine).fit()
print("< lm.summary() >")
print(im.summary())

