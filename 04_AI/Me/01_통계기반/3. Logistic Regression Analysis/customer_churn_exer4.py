# 목적: 로지스틱 모델을 통해 이탈 고객 예측하기
import numpy as np
import pandas as pd
import statsmodels.api as sm
from itertools import combinations
import operator

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in \
churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]
churn['churn'] = np.where(churn['churn'] == 'True.', 1, 0)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
						 churn['night_charge'] + churn['intl_charge']
churn['intl_plan'] = np.where(churn['intl_plan'] == 'yes', 1, 0)
churn['vmail_plan'] = np.where(churn['vmail_plan'] == 'yes', 1, 0)
# Fit a logistic regression model
dependent_variable = churn['churn']



match_dic={}
colums_list=['account_length', 'area_code', 'intl_plan', 'vmail_plan', 'vmail_message', 'day_mins', 'day_calls', 'day_charge', 'eve_mins', 'eve_calls', 'eve_charge', 'night_mins', 'night_calls', 'night_charge', 'intl_mins', 'intl_calls', 'intl_charge', 'custserv_calls','total_charges']
len_colums = len(colums_list)

dependent_variable = churn['churn']
for num in range(9,len_colums+1):
	combi_list = list(combinations(colums_list, num))
	if num == 2:
		print("debug")
		pass

	for tup in combi_list:
		column_list_combi = list(tup)
		independent_variables = churn[column_list_combi]
		independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
		logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()
		match_count = 0
		new_observatios = churn.loc[:, independent_variables.columns]
		new_observatios_with_constant = sm.add_constant(new_observatios, prepend=True)
		y_predicted = logit_model.predict(new_observatios_with_constant)
		y_predicted_rounded = [round(score, 0) for score in y_predicted]
		for index in range(len(y_predicted_rounded)):
			if y_predicted_rounded[index] == dependent_variable.values[index]:
				match_count += 1
		print(f'\n독립변수 조합 >> {column_list_combi}')
		print('>> match count=', match_count)
		print('>> 정답률: %.2f %%' % (match_count / len(y_predicted_rounded) * 100))
		match_dic[' '.join(column_list_combi)] = match_count / len(y_predicted_rounded) * 100

# 정답률 최대값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)
# print(match_dic)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d'%len(match_dic))
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0],match_dic[0][1]))


#  독립변수 최적화 분석 결과
# 총 조합 갯수: 354522
# MAX 조합: account_length intl_plan vmail_message day_calls eve_calls night_calls intl_mins intl_calls intl_charge >> 86.74 %