# 통계 모델: 선형회귀 분석 (Linear Regression Analysis)
# 목표 정답률: 독립변수를 모두 조합 한 결과 약 53.0244%를 초과한 정답률

import pandas as pd
from sklearn import svm, model_selection
import operator
from itertools import combinations

print("결과 예측하기")
wine = pd.read_csv('white_winequality.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

match_dic={}

# 전체 독립변수 식별
colums_list = ['alcohol','chlorides','citric_acid','density','fixed_acidity','free_sulfur_dioxide','pH',
               'residual_sugar','sulphates','total_sulfur_dioxide','volatile_acidity']
label = wine['quality']
# 최적의 독립변수 식별
for num in range(6,12):
    combi_list = list(combinations(colums_list,num))
    for tup in combi_list:
        # 종속 변수 식별
        data_header_list = list(tup)
        clf = svm.SVC(gamma='auto')
        scores = model_selection.cross_val_score(clf,wine[data_header_list],label, cv=5)

        accuracy = scores.mean()
        data_header_name = ' '.join(data_header_list)
        match_dic[data_header_name] = accuracy
        print(f'\n데이터 행 조합: {data_header_name}')
        print(f'>> 정답률: {accuracy*100} %%')


# 정답률 최대값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)
# print(match_dic)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d'%len(match_dic))
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0],match_dic[0][1]))
