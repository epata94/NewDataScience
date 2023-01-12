# 데이터 출처 : https://www.kaggle.com/shivam2503/diamonds
# 데이터 필드의 의미
# 13열: 종속변수 => 다이아몬드 등급
# 2열,4~8열: 다이아몬드 특성 (컬러, 무게, 선명도  ..)

# 학습 목표: 데이터 셋에 최적화된 머신러닝 모델 선택
# 머신러닝 모델: RandomForestRegressor
# 머신러닝 모델 선정 사유: 예측값을 범주형에도 적용가능하며 이에 다른 머신러닝 대비 최고의 정답률을 보임
# 교차 검증 K 값: 4 (전체 데이터 수와 모든 독립변수 경우의 수를 고려해 결정)
# 훈련데이터, 검증데이터 선정:  4분할된 데이터셋을 기준으로 훈련 및 검증 데이터 분할
# 성능평가: 1순위 => 교차 검증에 의한 평균 정답률, 2순위 => 프로그램 수행 속도
# 목표 정답률: 50% 이상
# 측정 정답률
# 총 조합 갯수: 511, 1개~10개의 독립변수 조합
# MAX 조합: depth table price clarity01 x >> 68.00 %
# 프로그램 소요 시간:  0:00:49.714000
import pandas as pd
import operator
from itertools import combinations
from datetime import datetime
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

match_dic={}
cross_val = 4
start_combi = 1


print("최적의 독립변수 선정하기 (교차검증 적용) ")
wine = pd.read_csv('diamonds.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')
columns_change = ['color01','clarity01','cut01']
columns_ori = ['color','clarity','cut']

for index in range(len(columns_change)):
    wine[columns_change[index]] = 0

for index in range(len(columns_ori)):
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'Fair',1,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'Good', 2,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'Very Good', 3,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'Premium', 4,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'Ideal', 5,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'D', 7,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'E', 6,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'F', 5,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'G', 4,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'H', 3,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'I', 2,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'J', 1,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'I1', 1,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'SI2', 2,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'SI1', 3,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'VS2', 4,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'VS1', 5,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'VVS2', 6,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'VVS1', 7,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'IF', 8,wine[columns_change[index]])

# 전체 독립변수 식별
colums_list = ['carat','depth','table','price','color01','clarity01','x','y','z']
end_combi = len(colums_list)+1
label = wine['cut01']

start_time = datetime.now()

# 최적의 독립변수 식별
for num in range(start_combi, end_combi):
    combi_list = list(combinations(colums_list,num))
    for tup in combi_list:
        # 종속 변수 식별
        data_header_list = list(tup)
        clf = RandomForestRegressor()
        # clf.fit(wine[data_header_list],label)
        scores = cross_val_score(clf,wine[data_header_list],label, cv=cross_val)
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
