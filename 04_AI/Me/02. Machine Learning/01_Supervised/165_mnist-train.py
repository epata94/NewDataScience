from sklearn import model_selection, svm, metrics
# CSV 파일을 읽어 들이고 가공하기 --- (※1)
def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2: continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {"labels":labels, "images":images}
data = load_csv("./mnist/train.csv")
test = load_csv("./mnist/t10k.csv")
# 학습하기 --- (※2)
clf = svm.SVC()
clf.fit(data["images"], data["labels"])
# 예측하기 --- (※3)
predict = clf.predict(test["images"])
# 결과 확인하기 --- (※4)
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)
# 정답률 = 0.7884231536926147
# 정답률 => ac_score => accuracy => 정답수 / 전체 테스트 갯수
# TP+TN/TP+FN+FP+TN
# 0~9 는 예측 결과에서 나오는 label의 모든 유형
# True Positive(TP) : 실제 True인 정답을 True라고 예측 (정답)
# False Positive(FP) : 실제 False인 정답을 True라고 예측 (오답)
# False Negative(FN) : 실제 True인 정답을 False라고 예측 (오답)
# True Negative(TN) : 실제 False인 정답을 False라고 예측 (정답)
# Precision = TP / TP + FP
# 한 달동안 얼마나 맑은 날이 많았나?
# Recall = TP / TP+FN
# 한 달 동안 비온날이 하루밖에 없었다면?
# F1-score = Precision과 Recall의 보정값
#                 precision    recall  f1-score   support
#
#            0       0.87      0.93      0.90        42
#            1       0.81      1.00      0.89        67
#            2       0.84      0.69      0.76        55
#            3       0.87      0.57      0.68        46
#            4       0.76      0.75      0.75        55
#            5       0.63      0.80      0.71        50
#            6       0.97      0.67      0.79        43
#            7       0.74      0.86      0.79        49
#            8       0.91      0.72      0.81        40
#            9       0.71      0.81      0.76        54
#
#     accuracy                           0.79       501
#    macro avg       0.81      0.78      0.78       501
# weighted avg       0.80      0.79      0.79       501