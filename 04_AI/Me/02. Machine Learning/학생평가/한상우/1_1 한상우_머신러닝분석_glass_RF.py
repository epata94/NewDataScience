'''
# 데이터 출처: https://www.kaggle.com/uciml/glass/download
# 10열: 종속변수 => 유리 타입
# 1열~9열:독립변수 => 유리 특성 (굴절율, 나트륨, 망간, 알루미늄, 규소, 칼륨, 칼슘, 바륨, 철)
# >> 독립변수 최적화 분석 결과 Random Forest<<
# 총 조합 갯수: 502, 2개~10개의 독립변수 조합
# MAX 조합: RI Mg Al Ba >> 85.19 %
# 프로그램 소요 시간:0:00:08.720400
 >> 독립변수 최적화 분석 결과 Random Forest+ (cross + val) << 동일개념의 로직 중복
# 총 조합 갯수: 502, 2개~10개의 독립변수 조합
# MAX 조합: RI Mg Al Ba >> 72.15 %
# 프로그램 소요 시간:0:01:17.769000
'''
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
from sklearn import svm, model_selection
import operator
from itertools import combinations
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

start = datetime.now()
match_dic = {}
cross_val = 9
start_combi = 1


print("최적의 독립변수 선정하기 (교차검증 적용)")
glass = pd.read_csv('glass.csv', sep=',', header=0)
glass.columns = glass.columns.str.strip()

# print(glass.columns)

# 전체 독립변수 식별
colums_list = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
end_combi = len(colums_list)+1
label = glass['Type']


# 최적의 독립변수 식별
for num in range(start_combi, end_combi):
    combi_list = list(combinations(colums_list, num))
    for tup in combi_list:
        # 종속 변수 식별
        data_header_list = list(tup)
        # data_header_list = tup[0]
        data_train, data_test, label_train, label_test = train_test_split(glass[data_header_list], label)
        data_header_name = ' '.join(data_header_list)
        clf = RandomForestClassifier()
        clf.fit(data_train, label_train)

        ### RandomForest(복운추출, 동일크기)와 CV를  같이 사용하는 것은 아닐 듯,,bootstrap과 cv는 같은 기능
        scores = model_selection.cross_val_score(clf, glass[data_header_list], label, cv=cross_val)
        clf.fit(data_train, label_train)
        accuracy = scores.mean()
        data_header_name = ' '.join(data_header_list)
        accuracy_round = round(accuracy * 100, 2)
        match_dic[data_header_name] = accuracy_round
        print(f'\n데이터 행 조합: {data_header_name}')
        print(f'>> 평균 정답률(k={cross_val}): {accuracy_round}%')
        ###


        '''

        pre = clf.predict(data_test)
        ac_score = metrics.accuracy_score(label_test, pre)
        ac_score = round(ac_score*100, 2)
        cl_report = metrics.classification_report(label_test, pre)
        print("정답률 =", ac_score)
        # print("리포트 = \n", cl_report)
        match_dic[data_header_name] = ac_score
        print(f'\n데이터 행 조합: {data_header_name}')
        print(f'>> 정답률({accuracy_round}%')
        '''


# 정답률 최대값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)
end = datetime.now()
print("\n\n >> 독립변수 최적화 분석 결과 <<")
print(f'총 조합 갯수: {len(match_dic)}, {start_combi}개~{end_combi}개의 독립변수 조합')
print("MAX 조합: %s >> %.2f %%" % (match_dic[0][0], match_dic[0][1]))
print(f"프로그램 소요 시간:{end-start}")
