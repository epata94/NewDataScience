# 목적: 간단한 기술 통계 구하기
import pandas as pd

# Read the data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
# wine = pd.read_csv('winequality-both.csv', sep=',', header=1)
wine.columns = wine.columns.str.replace(' ', '_')

# print(wine.head())
print(wine.head(10))

print("변수별 요약통계 표시")
print(wine.describe())

print("\n특정 열의 유일값 찾기")
print(sorted(wine.quality.unique()))
# 데이터의 유형을 찾는데 적합
print(sorted(wine.type.unique()))
# 데이터의 유형을 찾는데 적합
print(sorted(wine.fixed_acidity.unique()))
# 데이터의 유형을 찾는데 적합

print("\n빈도 찾기")
print(wine.quality.value_counts())