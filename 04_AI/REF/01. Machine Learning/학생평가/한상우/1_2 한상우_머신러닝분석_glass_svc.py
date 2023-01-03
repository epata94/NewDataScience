'''
# 데이터 출처: https://www.kaggle.com/uciml/glass/download
# 10열: 종속변수 => 유리 타입
# 1열~9열:독립변수 => 유리 특성 (굴절율, 나트륨, 망간, 알루미늄, 규소, 칼륨, 칼슘, 바륨, 철)
#  >> 독립변수 최적화 분석 결과 <<
# 총 조합 갯수: 511, 1개~10개의 독립변수 조합
# MAX 조합: Na Al K Ca Ba >> 69.44 %
# 프로그램 소요 시간:0:00:19.102800
'''

import pandas as pd
from sklearn import svm, model_selection
import operator
from itertools import combinations
from datetime import datetime

start = datetime.now()
match_dic = {}
cross_val = 9
start_combi = 1


print("최적의 독립변수 선정하기 (교차검증 적용) ")
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
        clf = svm.SVC(gamma='auto')

        scores = model_selection.cross_val_score(clf, glass[data_header_list], label, cv=cross_val)
        accuracy = scores.mean()
        data_header_name = ' '.join(data_header_list)
        accuracy_round = round(accuracy*100,2)
        match_dic[data_header_name] = accuracy_round
        print(f'\n데이터 행 조합: {data_header_name}')
        print(f'>> 평균 정답률(k={cross_val}): {accuracy_round}%')

end = datetime.now()

# 정답률 최대값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)

print("\n\n >> 독립변수 최적화 분석 결과 <<")
print(f'총 조합 갯수: {len(match_dic)}, {start_combi}개~{end_combi}개의 독립변수 조합')
print("MAX 조합: %s >> %.2f %%" % (match_dic[0][0], match_dic[0][1]))
print(f"프로그램 소요 시간:{end-start}")
