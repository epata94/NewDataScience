# 목적: 고정변수값 예측하기
import pandas as pd
from statsmodels.formula.api import ols, glm
from datetime import datetime
import time

print("7.2.7 예측하기")
# wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine = pd.read_csv('white_winequality.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
# R 추천 결과
# my_formula = 'quality ~ alcohol + chlorides + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
# my_formula = 'quality ~ alcohol + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
# my_formula = 'quality ~ alcohol+citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
# my_formula = 'quality ~ alcohol + chlorides + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()

dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type'])]

# new_observations = wine.ix[:, independent_variables.columns]
new_observations = wine.loc[:, independent_variables.columns]

start = datetime.fromtimestamp(time.time())
y_predicted = lm.predict(new_observations)
end = datetime.fromtimestamp(time.time())

y_predicted_rounded = [round(score) for score in y_predicted]

total_count = 0
index = 0
total_number = len(y_predicted_rounded)
total_correct = 0
while index < total_number:
    print(f'{index+1}    |{y_predicted_rounded[index]}   |{dependent_variable[index]}')
    if y_predicted_rounded[index] == dependent_variable [index]:
        total_correct += 1
    index+=1

print(f'\n전체 관찰 계수: {total_number}')
print(f'정답수: {total_correct}')
print(f'정답률: {(total_correct/total_number)*100} %')

print(start)
print(end)
print(end-start)

# 전체
# 전체 관찰 계수: 6497
# 정답수: 3465
# 정답률: 53.33230721871634 %

# 화이트와인 <= 와인의 품종이 품질을 예측하는데 중요한 요소로 활용되고 있음
# 전체 관찰 계수: 4898
# 정답수: 2541
# 정답률: 51.878317680685996 %