# 목적: 선형회귀(Linear Regression) 분석
import pandas as pd
from statsmodels.formula.api import ols, glm

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()
#lm = glm(my_formula, data=wine, family=sm.families.Gaussian()).fit()
#lm = smf.glm(formula_all, data=wine_standardized, family=sm.families.Gaussian()).fit()
print("< lm.summary() >")
print(lm.summary())
#                             OLS Regression Results
# 보통최소 제곱법:OLS(Ordinary Least Squares)
# R-squared: 얼마나 선형회귀에 근접함을 나타내는가? 사회과학분야: 30%, 자연과학분야: 70%
# F-statistic: P-value (0.05보다 낮기 때문에 유의미한 결과다)
# ==============================================================================
# Dep. Variable:                quality   R-squared:                       0.292
# Model:                            OLS   Adj. R-squared:                  0.291
# Method:                 Least Squares   F-statistic:                     243.3
# Date:                Wed, 13 Mar 2019   Prob (F-statistic):               0.00
# Time:                        14:51:08   Log-Likelihood:                -7215.5
# No. Observations:                6497   AIC:                         1.445e+04
# Df Residuals:                    6485   BIC:                         1.454e+04
# Df Model:                          11
# Covariance Type:            nonrobust
# coef(회귀계수): 다른 독립 변수는 고정되어 있고 특정 독립변수가 1단위 변할 때 종속변수가 변화하는 평균
# ========================================================================================
#                            coef    std err          t      P>|t|      [0.025      0.975]
# ----------------------------------------------------------------------------------------
# Intercept: y절편 => 고정 상수
# Intercept               55.7627     11.894      4.688      0.000      32.447      79.079
# alcohol                  0.2670      0.017     15.963      0.000       0.234       0.300
# chlorides               -0.4837      0.333     -1.454      0.146      -1.136       0.168
# citric_acid             -0.1097      0.080     -1.377      0.168      -0.266       0.046
# density                -54.9669     12.137     -4.529      0.000     -78.760     -31.173
# fixed_acidity            0.0677      0.016      4.346      0.000       0.037       0.098
# free_sulfur_dioxide      0.0060      0.001      7.948      0.000       0.004       0.007
# pH                       0.4393      0.090      4.861      0.000       0.262       0.616
# residual_sugar           0.0436      0.005      8.449      0.000       0.033       0.054
# sulphates                0.7683      0.076     10.092      0.000       0.619       0.917
# total_sulfur_dioxide    -0.0025      0.000     -8.969      0.000      -0.003      -0.002
# volatile_acidity        -1.3279      0.077    -17.162      0.000      -1.480      -1.176
# ==============================================================================
# Omnibus:                      144.075   Durbin-Watson:                   1.646
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              324.712
# Skew:                          -0.006   Prob(JB):                     3.09e-71
# Kurtosis:                       4.095   Cond. No.                     2.49e+05
# ==============================================================================

print("="*80+"\n")
print("\nQuantities you can extract from the result:\n%s" % dir(lm))
print("\nCoefficients:\n%s" % lm.params)
print("\nCoefficient Std Errors:\n%s" % lm.bse)
print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
print("\nF-statistic: %.1f  P-value: %.2f" % (lm.fvalue, lm.f_pvalue))
print("\nNumber of obs: %d  Number of fitted values: %s" % (lm.nobs, len(lm.fittedvalues)))
