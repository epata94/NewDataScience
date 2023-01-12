'''
# 데이터 출처: https://www.kaggle.com/uciml/glass/download
# 10열: 종속변수 => 유리 타입
# 1열~9열:독립변수 => 유리 특성 (굴절율, 나트륨, 망간, 알루미늄, 규소, 칼륨, 칼슘, 바륨, 철)
#  >> 독립변수 최적화 분석 결과 <<
# 총 조합 갯수: 511, 1개~9개의 독립변수 조합
# MAX 조합: Na Mg Al Ba >> 51.40 %
# 프로그램 소요 시간:0:00:02.527200
'''

from sklearn.linear_model import LinearRegression
import pandas as pd
import operator
from itertools import combinations
from datetime import datetime

start = datetime.now()
match_dic = {}
# cross_val = 9
start_combi = 1


print("최적의 독립변수 선정하기 ")
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
        # Clustering 객체를 생성하고 모델을 학습 시킨다.
        data_header_list = list(tup)

        data = glass[data_header_list]
        clf = LinearRegression()
        clf.fit(glass[data_header_list], label)
        pre = clf.predict(glass[data_header_list])

        ok_num = 0
        for index, predict_data in enumerate(pre):
            if round(predict_data) == label[index]:
                ok_num += 1
        accuracy = ok_num / len(label)

        data_header_name = ' '.join(data_header_list)
        match_dic[data_header_name] = accuracy * 100
        print(f'\n 데이터 행 조합: {data_header_name}')
        print(f'>> 정답율: {accuracy * 100}%')

end = datetime.now()

# 정답률 최대값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)

print("\n\n >> 독립변수 최적화 분석 결과 <<")
print(f'총 조합 갯수: {len(match_dic)}, {start_combi}개~{end_combi}개의 독립변수 조합')
print("MAX 조합: %s >> %.2f %%" % (match_dic[0][0], match_dic[0][1]))
print(f"프로그램 소요 시간:{end-start}")
