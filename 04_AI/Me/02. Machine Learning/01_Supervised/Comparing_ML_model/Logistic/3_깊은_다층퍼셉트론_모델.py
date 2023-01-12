# 0. 사용할 패키지 불러오기
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from datetime import datetime
import pandas as pd
import random, re
from sklearn.model_selection import train_test_split
from keras import optimizers

start_time = datetime.now()
csv = pd.read_csv('heart.csv')

csv_data = csv[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']]
csv_label = csv["target"]
# 학습 전용 데이터와 테스트 전용 데이터로 나누기 --- (※3)
x_train, x_test, y_train, y_test = train_test_split(csv_data, csv_label)
# x_train = x_train.to_numpy()
# x_test = x_test.to_numpy()
# y_train = y_train.to_numpy()
# y_test = y_test.to_numpy()

# 1. 데이터셋 생성하기

# 2. 모델 구성하기
model = Sequential()
# model.add(Dense(32, input_dim=13, activation='relu'))
# model.add(Dense(16, input_dim=13, activation='relu'))
# model.add(Dense(64, input_dim=13, activation='relu'))
# model.add(Dense(64, activation='relu'))
model.add(Dense(64, input_dim=13, activation='relu'))
model.add(Dense(13, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 3. 모델 학습과정 설정하기
# rmsprop = optimizers.rmsprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0)
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
# model.compile(optimizer=rmsprop, loss='binary_crossentropy', metrics=['accuracy'])

# 4. 모델 학습시키기
from keras.callbacks import EarlyStopping
# early_stopping = EarlyStopping(patience=20) # 조기종료 콜백함수 정의
# early_stopping = EarlyStopping(patience=20) # 조기종료 콜백함수 정의 (val_loss 보면서)
early_stopping = EarlyStopping() # 조기종료 콜백함수 정의 (val_loss 보면서)
# hist = model.fit(x_train, y_train, epochs=2000, batch_size=32, callbacks=[early_stopping])
hist = model.fit(x_train, y_train, epochs=2000, batch_size=32)

# 5. 학습과정 살펴보기
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.set_ylim([0.0, 1.0])
acc_ax.set_ylim([0.0, 1.0])

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()

# 6. 모델 평가하기
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=32)
print('loss_and_metrics : ' + str(loss_and_metrics))