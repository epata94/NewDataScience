import numpy as np


class Perceptron(object):
    # 학습률은 보통 0~1사이의 값을 설정하고 일반적으로 0.01이 가장 좋은 성능을 보인다.
    # 0.01을 기준으로 튜닝을 하게 된다.
    # 학습률이 작을 수록 가중치 업데이트 되는 값이 작고 클 수록 가중치 업데이트 되는 값이 커진다.
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        rgen = np.random.RandomState(self.random_state)
        # scale: 표준 편차 0.01, size: 특성 개수(2) 보다 1개 크게 만든다. (절편 고려)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            # 전체 데이터 셋에 대해 가중치, 편향 업데이트
            for xi, target in zip(X, y):
                # 맞추면 update는 0, 양성클래스 틀리면 update = 2eta, 음성클래스 틀리면 -2eta
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, xi):
        """입력 계산: 단일 행의 데이터에 대해 계산"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, xi):
        """단위 계단 함수를 사용하여 클래스 레이블을 반환합니다"""
        return np.where(self.net_input(xi) >= 0.0, 1, -1)

import os
import pandas as pd

s = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
print('URL:', s)

df = pd.read_csv(s,
                 header=None,
                 encoding='utf-8')

y = df.iloc[0:100, 4].values
# setosa면 -1 아니면 1
y = np.where(y == 'Iris-setosa', -1, 1)

# 꽃받침 길이와 꽃잎 길이를 추출합니다
X = df.iloc[0:100, [0, 2]].values

pass

p = Perceptron()
p.fit(X,y)
pass