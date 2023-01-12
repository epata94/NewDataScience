# 데이터 출처 : https://www.kaggle.com/uciml/zoo-animal-classification
# 데이터 필드의 의미
# 18열: 종속변수 => 동물계 분류
# 2열~17열: 동물의 특성 (머리카락, 알, 우유..)

# 학습 목표: 데이터 셋에 최적화된 머신러닝 모델 선택
# 머신러닝 모델:RandomForestClassifier()
# 머신러닝 모델 선정 사유: 예측값을 범주형에도 적용가능하며 이에 다른 머신러닝 대비 최고의 정답률을 보임
# 교차 검증 K 값: 4 (전체 데이터 수와 모든 독립변수 경우의 수를 고려해 결정)
# 훈련데이터, 검증데이터 선정:  4분할된 데이터셋을 기준으로 훈련 및 검증 데이터 분할
# 성능평가: 1순위 => 교차 검증에 의한 평균 정답률, 2순위 => 프로그램 수행 속도
# 목표 정답률: 50% 이상
# 측정 정답률
# 총 조합 갯수: 65535, 1개~17개의 독립변수 조합
# MAX 조합: airborne aquatic backbone breathes domestic eggs feathers
# fins hair legs milk predator tail toothed venomous >> 99.11 %
# 프로그램 소요 시간:  1:04:24.620000
import pandas as pd
from sklearn import svm, model_selection
import operator
from itertools import combinations
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

match_dic={}
cross_val = 4
start_combi = 1


print("최적의 독립변수 선정하기 (교차검증 적용) ")
zoo = pd.read_csv('zoo.csv',sep=',',header=0)
zoo.columns = zoo.columns.str.replace(' ','_')


# 전체 독립변수 식별
# colums_list = ['hair',	'feathers',	'eggs',	'milk',	'airborne',
#                'aquatic',	'predator',	'toothed',	'backbone',
#                'breathes',	'venomous',	'fins',	'legs',	'tail',	'domestic',	'catsize']
colums_list = list(zoo.columns.difference(['class_type','animal_name']))

end_combi = len(colums_list)+1
label = zoo['class_type']

start_time = datetime.now()

# 최적의 독립변수 식별
for num in range(start_combi, end_combi):
    combi_list = list(combinations(colums_list,num))
    for tup in combi_list:
        # 종속 변수 식별
        data_header_list = list(tup)
        clf = RandomForestClassifier()
        # clf.fit(wine[data_header_list],label)
        scores = model_selection.cross_val_score(clf,zoo[data_header_list],label, cv=cross_val)
        accuracy = scores.mean()
        data_header_name = ' '.join(data_header_list)
        accuracy_round = round(accuracy*100,4)
        match_dic[data_header_name] = accuracy_round
        print(f'\n데이터 행 조합: {data_header_name}')
        print(f'>> 평균 정답률(K={cross_val}): {accuracy_round}%')

end_time = datetime.now()

# 정답률 최대값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)

print("\n\n 독립변수 최적화 분석 결과")
print(f'총 조합 갯수: {len(match_dic)}, {start_combi}개~{end_combi}개의 독립변수 조합')
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0],match_dic[0][1]))
print("프로그램 소요 시간: ", end_time-start_time)
