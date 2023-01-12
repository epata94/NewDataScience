# 목적: 새로운 변수 total_charges를 기준으로 그룹화한 뒤
#       그룹 별 통계량 구하기
import numpy as np
import pandas as pd

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in \
churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)

churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
						 churn['night_charge'] + churn['intl_charge']
# cut(데이터 객체, 구간수, precision=)
# 데이터 객체, 구간수 필수 인자
# 구간수: 구간 균등 분할 (갯수에 따른 분할은 qcut)
# precision 소수점 이하 자릿수
factor_cut = pd.cut(churn.total_charges, 5, precision=2)
def get_stats(group):
	return {'min' : group.min(), 'max' : group.max(),
			'count' : group.count(), 'mean' : group.mean(),
			'std' : group.std()}
grouped = churn.custserv_calls.groupby(factor_cut)
print(grouped.apply(get_stats).unstack())
pass

