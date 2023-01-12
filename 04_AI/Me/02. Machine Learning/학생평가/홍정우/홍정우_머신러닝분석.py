# 데이터 출처 : https://www.kaggle.com/datasnaek/chess
# 데이터 필드의 의미
# 7열: 종속변수 => winner
# 2열,3열,4열,9열,11열: 체스 승패 승률 (턴수, 등급 ..)

# 학습 목표: 데이터 셋에 최적화된 머신러닝 모델 선택
# 머신러닝 모델: SVC
# 머신러닝 모델 선정 사유: 예측값을 범주형에도 적용가능하며 이에 다른 머신러닝 대비 최고의 정답률을 보임
# 교차 검증 K 값: 고려 않함
# 훈련데이터, 검증데이터 선정:  N/A
# 성능평가: 1순위 => 정답률, 2순위 => 프로그램 수행 속도
# 목표 정답률: 선형회귀 통계 모델의 최고정답률(50.88%) 이상
# 측정 정답률
#  독립변수 최적화 분석 결과
# 총 조합 갯수: 6, 4개~20059개의 독립변수 조합
# MAX 조합: last_move_at turns white_rating black_rating >> 52.64 %
# 프로그램 소요 시간:  0:04:14.195000

import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import csv

import pandas as pd
from sklearn import svm,metrics
from sklearn.model_selection import train_test_split
import operator
from itertools import combinations
from datetime import datetime

match_dic={}
start_combi = 4


print("최적의 독립변수 선정하기 (교차검증 적용) ")
csv = pd.read_csv('games.csv',sep=',',header=0)
#csv.columns = csv.columns.str.replace(' ','_')


# 전체 독립변수 식별
colums_list = csv[["created_at","last_move_at","turns","white_rating","black_rating"]]
end_combi = len(colums_list)+1
label = csv['winner']

start_time = datetime.now()

# 최적의 독립변수 식별
for num in range(start_combi, end_combi):
    combi_list = list(combinations(colums_list,num))
    for tup in combi_list:
        # 종속 변수 식별
        data_header_list = list(tup)
        clf = svm.SVC(gamma='auto')
        train_data, test_data, train_label, test_label = \
        train_test_split(csv[data_header_list],label)
        clf.fit(train_data, train_label)
        pre = clf.predict(test_data)
        ac_score = metrics.accuracy_score(test_label, pre)
        data_header_name = ' '.join(data_header_list)
        accuracy_round = round(ac_score*100,4)
        match_dic[data_header_name] = accuracy_round
        print(f'\n데이터 행 조합: {data_header_name}')
        print(f'>> 정답률: {accuracy_round}%')

end_time = datetime.now()

# 정답률 최대값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)

print("\n\n 독립변수 최적화 분석 결과")
print(f'총 조합 갯수: {len(match_dic)}, {start_combi}개~{end_combi}개의 독립변수 조합')
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0],match_dic[0][1]))
print("프로그램 소요 시간: ", end_time-start_time)
