# 데이터 출처: kaggle
# 데이터 개요: 51490건의 League of legends 게임 데이터
# 데이터 예측 모델: 이진클래스
# 적용 머신러닝 모델: 깊은 다층 퍼셉트론 신경망
# 훈련 데이터셋: 38617 건
# 검증 데이터셋: 12873 건
# 시험 데이터셋: 수집데이터로서 시험셋을 확보할 수 없으므로 고려하지 않음
# 입력 데이터: 58 항목의 게임데이터
# 은닉층: 2개
# 출력 데이터: 2개 (1:purple, 0:blue)
# 사용한 활성화 함수
# - 제1 은닉층: Relu
# - 제2 은닉층: Relu
# - Output Layer: Sigmoid
# 사용한 손실함수: binary_crossentropy
# 사용한 Optimizer: rmsprop
# Tensorflow 버전: 2.0.0
# 파이썬버전: 3.7.4

import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
import keras

match_dic={}

wine = pd.read_csv('diamonds.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')
columns_change = ['color01','clarity01','cut01']
columns_ori = ['color','clarity','cut']

for index in range(len(columns_change)):
    wine[columns_change[index]] = 0

for index in range(len(columns_ori)):
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'Fair',0,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'Good', 1,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'Very Good', 2,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'Premium', 3,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'Ideal', 4,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'D', 7,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'E', 6,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'F', 5,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'G', 4,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'H', 3,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'I', 2,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'J', 1,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'I1', 1,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'SI2', 2,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'SI1', 3,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'VS2', 4,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'VS1', 5,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'VVS2', 6,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'VVS1', 7,wine[columns_change[index]])
    wine[columns_change[index]] = np.where(wine[columns_ori[index]] == 'IF', 8,wine[columns_change[index]])

# 전체 독립변수 식별
input_data_header=['carat','depth','table','price','color01','clarity01','x','y','z']
input_data_number = len(input_data_header)
label = wine['cut01']

start_time = datetime.now()

train_data, test_data, train_label, test_label = train_test_split(wine[input_data_header],label)
train_label = to_categorical(train_label, num_classes=5)
test_label = to_categorical(test_label, num_classes=5)
# 2. 모델 구성하기
model = Sequential()
model.add(Dense(64, input_dim=input_data_number, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(5, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# 4. 모델 학습시키기
tb_hist = keras.callbacks.TensorBoard(log_dir='./graph', histogram_freq=0, write_graph=True, write_images=True)
# hist = model.fit(train_data, train_label, epochs=30, batch_size=32, validation_data=(test_data, test_label))
# hist = model.fit(train_data, train_label, epochs=1000, batch_size=32, validation_data=(test_data, test_label))
hist = model.fit(train_data, train_label, epochs=10000, batch_size=32, validation_data=(test_data, test_label))
# hist = model.fit(train_data, train_label, epochs=500, batch_size=32)
# hist = model.fit(train_data, train_label, epochs=4000, batch_size=32)

# 5. 학습과정 살펴보기
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
acc_ax.plot(hist.history['val_accuracy'], 'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()


# 6. 모델 평가하기
loss_and_metrics = model.evaluate(test_data, test_label, batch_size=32)
print('loss_and_metrics : ' + str(loss_and_metrics))