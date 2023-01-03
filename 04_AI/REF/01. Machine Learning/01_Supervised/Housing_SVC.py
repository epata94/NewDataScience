# 총 조합 갯수 = 2047
# 5% MAX 조합: stories prefarea01 >> 22.48 %
# 10% MAX 조합: stories recroom01 fullbase01
# gashw01 airco01 garagepl prefarea01 >> 36.43 %
# 20% MAX 조합: bedrooms stories driveway01 recroom01
# fullbase01 airco01 prefarea01 >> 60.47 %
# 프로그램 소요 시간:  0:03:23.795301

import pandas as pd
import numpy as np
from sklearn import metrics, svm
from itertools import combinations
import operator
from datetime import datetime
from sklearn.model_selection import train_test_split

start_time = datetime.now()
print("< Housing Predict >")
house = pd.read_csv('Housing.csv', sep=',', header=0)
columns_change = ['driveway01','recroom01','fullbase01','gashw01','airco01','prefarea01']
columns_ori = ['driveway','recroom','fullbase','gashw','airco','prefarea']

for index in range(len(columns_ori)):
    house[columns_change[index]] = np.where(house[columns_ori[index]] == 'yes',1,0)

label = house['price']
independent_variables_list = ['lotsize','bedrooms','bathrms','stories','driveway01',
                              'recroom01','fullbase01','gashw01','airco01','garagepl','prefarea01']

delta_plus = lambda x,y:x+x*y
delta_minus = lambda x,y:x-x*y
match_dic_5 = {}
match_dic_10 ={}
match_dic_20 = {}

for num in range(1,12):
    combi_list = list(combinations(independent_variables_list, num))
    for tup in combi_list:
        data_header_list = list(tup)
        data_header_name = ' '.join(data_header_list)

        data_train, data_test, label_train, label_test = train_test_split(house[data_header_list], label)
        clf = svm.SVC()
        clf.fit(data_train, label_train)
        y_predicted = clf.predict(data_test)

        match_count_5 = 0
        match_count_10 = 0
        match_count_20 = 0
        for index, lab in enumerate(label_test):
            ### 5%
            if delta_minus(lab, 0.05) < y_predicted[index] < \
            delta_plus(lab, 0.05):
                match_count_5 += 1
            ### 10%
            if delta_minus(lab, 0.1) < y_predicted[index] < \
                    delta_plus(lab, 0.1):
                match_count_10 += 1
            ### 20%
            if delta_minus(lab, 0.2) < y_predicted[index] < \
                    delta_plus(lab, 0.2):
                match_count_20 += 1

        print('\n>> ', data_header_name)
        print('>> 5% match count= ',match_count_5)
        print('>> 10% match count= ',match_count_10)
        print('>> 20% match count= ',match_count_20)
        print('>> 5%% 정답률: %.2f %% '%(match_count_5 / len(y_predicted) * 100))
        print('>> 10%% 정답률: %.2f %% '%(match_count_10 / len(y_predicted) * 100))
        print('>> 20%% 정답률: %.2f %% '%(match_count_20 / len(y_predicted) * 100))
        match_dic_5['%s' %data_header_name] = match_count_5 / len(y_predicted)*100
        match_dic_10['%s' %data_header_name] = match_count_10 / len(y_predicted)*100
        match_dic_20['%s' %data_header_name] = match_count_20 / len(y_predicted)*100

###  최댓값 찾기
match_dic_5 = sorted(match_dic_5.items(),key=operator.itemgetter(1),reverse=True)
match_dic_10 = sorted(match_dic_10.items(),key=operator.itemgetter(1),reverse=True)
match_dic_20 = sorted(match_dic_20.items(),key=operator.itemgetter(1),reverse=True)
print(match_dic_5)
print(match_dic_10)
print(match_dic_20)
print('총 조합 갯수 = %d'%(len(match_dic_5)))
print('5%% MAX 조합: %s >> %.2f %%'%(match_dic_5[0][0],match_dic_5[0][1]))
print('10%% MAX 조합: %s >> %.2f %%'%(match_dic_10[0][0],match_dic_10[0][1]))
print('20%% MAX 조합: %s >> %.2f %%'%(match_dic_20[0][0],match_dic_20[0][1]))
end_time = datetime.now()
print("프로그램 소요 시간: ", end_time-start_time)
