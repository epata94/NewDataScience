# 목적: 로지스틱 모델을 통해 이탈 고객 예측하기
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in \
churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]
churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
						 churn['night_charge'] + churn['intl_charge']

# Fit a logistic regression model
dependent_variable = churn['churn01']

independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()

new_observatios = churn.ix[churn.index.isin(range(20)), independent_variables.columns]
new_observatios_with_constant = sm.add_constant(new_observatios, prepend=True)
y_predicted = logit_model.predict(new_observatios_with_constant)
y_predicted_rounded=[round(score,0) for score in y_predicted]
print(y_predicted_rounded)
logistic_predicted_value_list=[]
for predict_value in y_predicted_rounded:
	if predict_value==0.0:
		logistic_predicted_value_list.append(False)
	else:
		logistic_predicted_value_list.append(True)
print(logistic_predicted_value_list)
