# 범주형 데이터(독립변수)가 문자이기 때문에 수치형으로 변환시킬때 주의할 점
# 범주형 데이터 정규화하기
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
# 데이터 읽어 들이기
mr = pd.read_csv("mushroom.csv", header=None)
# 데이터 내부의 분류 변수 전개하기
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows():
    label.append(row.ix[0])
    exdata = []
    for col, v in enumerate(row.ix[1:]):
        if row_index == 0:
            attr = {"dic": {}, "cnt":0}
            attr_list.append(attr)
        else:
            attr = attr_list[col]
        # 버섯의 특징 기호를 배열로 나타내기
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
        if v in attr["dic"]:
            idx = attr["dic"][v]
        else:
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] += 1
        d[idx] = 1
        exdata += d
    data.append(exdata)
# 학습 전용 데이터와 테스트 전용 데이터로 나누기
data_train, data_test, label_train, label_test = \
train_test_split(data, label)
# 데이터 학습시키기
clf = RandomForestClassifier()
clf.fit(data_train, label_train)
# 데이터 예측하기
predict = clf.predict(data_test)
# 결과 테스트하기
ac_score = metrics.accuracy_score(label_test, predict)
print("정답률 =", ac_score)

feature_list = list(data_test.columns)

# Get numerical feature importances
importances = list(clf.feature_importances_)
# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
# Sort the feature importances by most important first
#feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
# Print out the feature and importances 
#[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances]
#print(feature_importances)
feature_importances_df = pd.DataFrame.from_records(feature_importances, columns=['feature','importance'])

print(feature_importances_df)
'''
feature_importances_df['tstmp'] = timestamp
feature_importances_df['model'] = model
feature_importances_df['importance'].fillna(0, inplace=True)
feature_importances_df['importance'] = round(feature_importances_df['importance'])
'''
# <class 'list'>: attr_list
# 초기값 (열 기준)
# [{'dic': {}, 'cnt': 0}]
# [{'dic': {'x': 0}, 'cnt': 1}]
# [{'dic': {'x': 0},{'b': 1}, 'cnt': 2}]
#
# <class 'list'>: [{'dic': {'x': 0}, 'cnt': 1}, {'dic': {'s': 0}, 'cnt': 1}, {'dic': {'n': 0}, 'cnt': 1}, {'dic': {'t': 0}, 'cnt': 1}, {'dic': {'p': 0}, 'cnt': 1}, {'dic': {'f': 0}, 'cnt': 1}, {'dic': {'c': 0}, 'cnt': 1}, {'dic': {'n': 0}, 'cnt': 1}, {'dic': {'k': 0}, 'cnt': 1}, {'dic': {'e': 0}, 'cnt': 1}, {'dic': {'e': 0}, 'cnt': 1}, {'dic': {'s': 0}, 'cnt': 1}, {'dic': {'s': 0}, 'cnt': 1}, {'dic': {'w': 0}, 'cnt': 1}, {'dic': {'w': 0}, 'cnt': 1}, {'dic': {'p': 0}, 'cnt': 1}, {'dic': {'w': 0}, 'cnt': 1}, {'dic': {'o': 0}, 'cnt': 1}, {'dic': {'p': 0}, 'cnt': 1}, {'dic': {'k': 0}, 'cnt': 1}, {'dic': {'s': 0}, 'cnt': 1}, {'dic': {'u': 0}, 'cnt': 1}]
#
# 모든 열에서 나올 수 있는 문자열의 종류 및 문자열 별 인덱스
# ex)첫번째 데이터(독립변수) 열: cap-shape
# {'dic': { [문자] : [문자의 인덱스], ....}, 'cnt':[다음에 등록할 인덱스]
# {'dic': {'x': 0, 'b': 1, 's': 2, 'f': 3, 'k': 4, 'c': 5}, 'cnt': 6}
# x: 100000
# b: 010000
# s: 001000
# f: 000100
# k: 000010
# c: 000001
# [
# {'dic': {'x': 0, 'b': 1, 's': 2, 'f': 3, 'k': 4, 'c': 5}, 'cnt': 6},
# {'dic': {'s': 0, 'y': 1, 'f': 2, 'g': 3}, 'cnt': 4},
# {'dic': {'n': 0, 'y': 1, 'w': 2, 'g': 3, 'e': 4, 'p': 5, 'b': 6, 'u': 7, 'c': 8, 'r': 9}, 'cnt': 10},
# {'dic': {'t': 0, 'f': 1}, 'cnt': 2}, {'dic': {'p': 0, 'a': 1, 'l': 2, 'n': 3, 'f': 4, 'c': 5, 'y': 6, 's': 7, 'm': 8}, 'cnt': 9}, {'dic': {'f': 0, 'a': 1}, 'cnt': 2}, {'dic': {'c': 0, 'w': 1}, 'cnt': 2}, {'dic': {'n': 0, 'b': 1}, 'cnt': 2}, {'dic': {'k': 0, 'n': 1, 'g': 2, 'p': 3, 'w': 4, 'h': 5, 'u': 6, 'e': 7, 'b': 8, 'r': 9, 'y': 10, 'o': 11}, 'cnt': 12}, {'dic': {'e': 0, 't': 1}, 'cnt': 2}, {'dic': {'e': 0, 'c': 1, 'b': 2, 'r': 3, '?': 4}, 'cnt': 5}, {'dic': {'s': 0, 'f': 1, 'k': 2, 'y': 3}, 'cnt': 4}, {'dic': {'s': 0, 'f': 1, 'y': 2, 'k': 3}, 'cnt': 4}, {'dic': {'w': 0, 'g': 1, 'p': 2, 'n': 3, 'b': 4, 'e': 5, 'o': 6, 'c': 7, 'y': 8}, 'cnt': 9}, {'dic': {'w': 0, 'p': 1, 'g': 2, 'b': 3, 'n': 4, 'e': 5, 'y': 6, 'o': 7, 'c': 8}, 'cnt': 9}, {'dic': {'p': 0}, 'cnt': 1}, {'dic': {'w': 0, 'n': 1, 'o': 2, 'y': 3}, 'cnt': 4}, {'dic': {'o': 0, 't': 1, 'n': 2}, 'cnt': 3}, {'dic': {'p': 0, 'e': 1, 'l': 2, 'f': 3, 'n': 4}, 'cnt': 5}, {'dic': {'k': 0, 'n': 1, 'u': 2, 'h': 3, 'w': 4, 'r': 5, 'o': 6, 'y': 7, 'b': 8}, 'cnt': 9}, {'dic': {'s': 0, 'n': 1, 'a': 2, 'v': 3, 'y': 4, 'c': 5}, 'cnt': 6}, {'dic': {'u': 0, 'g': 1, 'm': 2, 'd': 3, 'p': 4, 'w': 5, 'l': 6}, 'cnt': 7}]
#
#
#
# <class 'list'>: [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ... ]