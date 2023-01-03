import pandas as pd
from sklearn import svm, metrics
# XOR 연산
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기 --- (※1)
xor_df = pd.DataFrame(xor_input)
xor_data  = xor_df.iloc[:,0:2] # 데이터
xor_label = xor_df.iloc[:,2]   # 레이블
# 데이터 학습과 예측하기 --- (※2)
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)
# 정답률 구하기 --- (※3)
# normalize: default 값 True <= 정답률, False인 경우 정답 개수
ac_score = metrics.accuracy_score(xor_label, pre)
# ac_score = metrics.accuracy_score(xor_label, pre, normalize=True)
# ac_score = metrics.accuracy_score(xor_label, pre, normalize=False)
print("정답률 =", ac_score)