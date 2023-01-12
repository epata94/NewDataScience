# 목적: 로지스틱 모델을 통해 이탈 고객 예측하기
import numpy as np
import pandas as pd
import statsmodels.api as sm

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

# independent_variables = churn[['account_length', 'area_code', 'intl_plan', 'vmail_plan', 'vmail_message', 'day_mins', 'day_calls', 'day_charge', 'eve_mins', 'eve_calls', 'eve_charge', 'night_mins', 'night_calls', 'night_charge', 'intl_mins', 'intl_calls', 'intl_charge', 'custserv_calls', 'total_charges']]
independent_variables = churn[['account_length', 'area_code', 'intl_plan', 'vmail_plan', 'vmail_message', 'day_mins', 'day_calls', 'day_charge', 'eve_mins', 'eve_calls', 'eve_charge', 'night_mins', 'night_calls', 'night_charge', 'intl_mins', 'intl_calls', 'intl_charge', 'custserv_calls']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()

logit_model.summary()
print("\nCoefficients:\n%s" % logit_model.params)
