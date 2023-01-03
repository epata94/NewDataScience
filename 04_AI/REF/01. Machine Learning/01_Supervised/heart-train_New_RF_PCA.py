import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
# 데이터 읽어 들이기--- (※1)
mr = pd.read_csv("heart.csv" )
# 데이터 내부의 기호를 숫자로 변환하기--- (※2)
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows():
    # 분류형인 라벨은 타입이 문자여도 상관없음
    label.append(row.ix[13])
    row_data = []
    for v in row.ix[:12]:
        # 하지만 데이터(독립변수)는 문자일 경우 에러를 발생한다.
        row_data.append(v)
    data.append(row_data)
# 학습 전용과 테스트 전용 데이터로 나누기 --- (※3)
print(data)
print(mr.columns)
data_train, data_test, label_train, label_test = \
    train_test_split(data, label)
# 데이터 학습시키기 --- (※4)
clf = RandomForestClassifier(n_jobs=-1, n_estimators=500, max_depth=5, min_samples_leaf=5, min_samples_split=5, max_features="auto")
# clf = RandomForestClassifier()
clf.fit(data_train, label_train)
# 데이터 예측하기 --- (※5)
predict = clf.predict(data_test)
# 결과 테스트하기 --- (※6)
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)

feature_list = list(mr.columns)

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