# 목적: 그룹화, 히스토그램
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read the data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

# Display descriptive statistics for quality by wine type
print("< 와인 종류에 따른 기술통계를 출력하기 >")
# 엑셀의 피벗 테이블 효과
print('\n')
print(wine['alcohol'])
print('\n')
print(wine.groupby('type')[['alcohol']].describe())
print('\n')
print(wine.groupby('type')[['alcohol']].describe().unstack('type'))
print('\n')

# Calculate specific quantiles
print("< 특정 사분위수 계산하기 >")
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

print("\n"+'='*80)
print("7.2.2 그룹화, 히스토그램, t 검정")
# red_wine = wine.ix[wine['type']=='red', 'quality']
# ix함수는 현재 deprecate되었음. 현재 파이썬 버전에서 공식적으로 지원되지는 않고
# 다만 하위 파이썬 호환을 위해서 수행시 warning 메세지를 보여주고 정상동작한다.
red_wine = wine.loc[wine['type']=='red', 'quality']
# white_wine = wine.ix[wine['type']=='white', 'quality']
white_wine = wine.loc[wine['type']=='white', 'quality']

sns.set_style("dark")
print(sns.distplot(red_wine, \
		norm_hist=True, kde=False, color="red", label="Red wine"))
print(sns.distplot(white_wine, \
		norm_hist=True, kde=False, color="white", label="White wine"))
# sns.axlabel("Quality Score", "Density")
plt.xlabel("Quality Score")
plt.ylabel("Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
plt.show()

# Test whether mean quality is different between red and white wines
print("\n와인의 종류에 따라 품질의 차이 검정")
print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)

print('\nT-Test')
print('p-value: %.4f' %  pvalue)
# pvalue: 유의확률 (통계값을 얼마나 신뢰할 수 있는가를 나타내는 지표)
# pvalue가 0.05 보다 작으면 기무가설(두 표본과의 차이가 없다,유의 결과)를 기각할 수 있다.
# t 검정(t-test) 서로 다른 두 그룹 간 평균의 차이가 유의미한지를 검정하는 통계적인 방법으로
# 샘플이 등분산성, 독립성을 충족하고 정규성이 부족할 경우 경우 적용할 수 있다.
# 이 예제에서 두 샘플은 독립이고,
# 표준편차가 작으므로 등분산성을 충족한다고 볼 수 있다.
# 히스토그램과 개수(30개 이상)로 볼 때 정규분포 데이터를 활용해도 좋다.
