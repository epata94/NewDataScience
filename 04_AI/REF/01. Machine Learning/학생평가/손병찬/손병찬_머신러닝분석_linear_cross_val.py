# 데이터 출처 : https://www.kaggle.com/ronitf/heart-disease-uci/
# 데이터 필드의 의미
# 14열: 종속변수 => 심장병 유무
# 1열~13열: 환자의 신체 정보(나이, 성별, 가슴통증타입, 혈압 ...)

# 학습 목표: 데이터 셋에 최적화된 머신러닝 모델 선택
# 머신러닝 모델: LinearRegression
# 머신러닝 모델 선정 사유: 타 러신모델과 정답률, 속도 비교 분석을 위해 선정
# 교차 검증 K 값: 7 (전체 데이터 수와 모든 독립변수 경우의 수를 고려해 결정)
# 훈련데이터, 검증데이터 선정: 7분할된 데이터셋을 기준으로 훈련 및 검증 데이터 분할
# 성능평가: 1순위 => 교차 검증에 의한 평균 정답률, 2순위 => 프로그램 수행 속도
# 목표 정답률: 50% 이상

# 독립변수 최적화 분석 결과
# 총 조합 갯수: 8191, 1개~14개의 독립변수 조합
# MAX 조합: sex cp trestbps chol fbs restecg thalach slope ca thal >> 85.81 %
# 프로그램 소요 시간:  0:00:53.066500

import pandas as pd
from sklearn import svm, model_selection, metrics
import operator
from itertools import combinations
from datetime import datetime
from sklearn.linear_model import LinearRegression
import random, re

start_time = datetime.now()
match_dic={}
cross_val = 7
start_combi = 1
print("최적의 독립변수 선정하기 (교차검증 적용) ")
lines = open('heart.csv', 'r', encoding='utf-8').read().split('\n')
f_tonum = lambda  n : float(n) if re.match(r'^[0-9\.]+$', n) else n
f_cols = lambda li: list(map(f_tonum, li.strip().split(',')))
csv = list(map(f_cols, lines))
del csv[0]
random.shuffle(csv)  # 데이터 섞기
# 전체 독립변수 식별
colums_list = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']
end_combi = len(colums_list)+1
# 데이터를 k개로 분할하기
csvk = [[] for i in range(cross_val)]
for i in range(len(csv)):
    csvk[i % cross_val].append(csv[i])
# 리스트를 데이터와 라벨과 분류하는 함수
def split_data_label(rows):
    data = []
    label = []
    for row in rows:
        temp_list = []
        for i in header_num_list:
            temp_list.append(row[i])
        data.append(temp_list)
        label.append(row[len(colums_list)])
    return (data, label)
# 정답률 구하기
def calc_score(test, train):
    test_f, test_l = split_data_label(test)
    train_f, train_l = split_data_label(train)
    # 학습시키고 정답률 구하기
    clf = LinearRegression()
    clf.fit(train_f, train_l)
    predict = clf.predict(test_f)
    ok_num = 0
    for index, t_data in enumerate(test_l):
        if round(predict[index]) == t_data:
            ok_num += 1
    return (ok_num / len(predict))
# 최적의 독립변수 식별
for num in range(start_combi, end_combi):
    combi_list = list(combinations(colums_list,num))
    for tup in combi_list:
        # 종속 변수 식별
        data_header_list = list(tup)
        # 데이터 해더 번호 식별
        header_num_list = []
        for data in data_header_list:
            for num, col in enumerate(colums_list):
                if data == col:
                    header_num_list.append(num)
                    break
        # k개로 분할해서 정답률 구하기
        score_list = []
        for testc in csvk:
            # testc 이외의 데이터를 훈련 전용 데이터로 사용하기
            trainc = []
            for i in csvk:
                if i != testc: trainc += i
            sc = calc_score(testc, trainc)
            score_list.append(sc)
        print("각각의 정답률 =", score_list)
        accuracy = sum(score_list) / len(score_list)
        accuracy_round = round(accuracy*100, 4)
        data_header_name = ' '.join(data_header_list)
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