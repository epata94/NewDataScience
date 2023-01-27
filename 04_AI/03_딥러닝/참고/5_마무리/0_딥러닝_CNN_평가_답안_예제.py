# 데이터 출처: keras 내장 모듈
# 데이터 개요: 약 7만건에 해당하는 손글씨 데이터 셋
# 데이터 예측 모델: 다중클래스
# 적용 머신러닝 모델: CNN
# 훈련 데이터셋: 5만건
# 검증 데이터셋: 1만건
# 시험 데이터셋: 1만건
# 입력 데이터: 28*28 픽셀데이터
# 은닉층: 6개(Featering Layer: 4개, Fully Connected Layer: 2개)
# 출력 데이터: 10개 Class (0~9까지의 숫자)
# 사용한 활성화 함수
# - Convolution Layer: Relu
# - Output Layer: Softmax
# 사용한 손실함수: categorical_crossentropy
# 사용한 Optimizer: sgd
# Tensorflow 버전: 2.0.0
# 파이썬버전: 3.7.4
import numpy as np
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten

width = 28
height = 28

# 1. 데이터셋 생성하기

# 훈련셋과 시험셋 불러오기
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, width, height, 1).astype('float32') / 255.0
x_test = x_test.reshape(10000, width, height, 1).astype('float32') / 255.0

# 훈련셋과 검증셋 분리
x_val = x_train[50000:]
y_val = y_train[50000:]
x_train = x_train[:50000]
y_train = y_train[:50000]

# 데이터셋 전처리 : one-hot 인코딩
y_train = np_utils.to_categorical(y_train)
y_val = np_utils.to_categorical(y_val)
y_test = np_utils.to_categorical(y_test)

# 2. 모델 구성하기
model = Sequential()
# Conv2D 레이어: 이미지 처리에 주로 사용하는 레이어, 이미지의 특징을 추출한다.
# 첫번째 인자: 컴볼루션 필터 수
# 두번째 인자: 컨볼루션 커널의 (행,열)
# input_shape: 입력 형태 정의 (행, 열, 채널수),
#             일반적으로 흑백 이미지는 1, 컬러(RGB)인 경우는 3으로 셋팅한다.
# 필터는 일반적으로 (4,4) 또는 (3,3)과 같은 정사각 행렬로 정의된다.
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(width, height, 1)))

# MaxPooling2D: 이미지의 특징을 단순화 시킨다. => 사소한 변화에도 일정한 예측을 하기 위하여
# pool_size: 수직, 수평 축소 비율을 지정한다. ex) (2,2) 인 경우 이미지의 크기를 반으로 줄어든다.
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
# 이미지를 일차원으로 바꿔주는 Flatten 레이어
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(10, activation='softmax'))

# 3. 모델 학습과정 설정하기
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# 4. 모델 학습시키기
hist = model.fit(x_train, y_train, epochs=30, batch_size=32, validation_data=(x_val, y_val))

# 5. 학습과정 살펴보기
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')
loss_ax.set_ylim([0.0, 0.5])

acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
acc_ax.plot(hist.history['val_accuracy'], 'g', label='val acc')
acc_ax.set_ylim([0.8, 1.0])

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()

# 6. 모델 평가하기
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=32)
print('## evaluation loss and_metrics ##')
print(loss_and_metrics)

# 7. 모델 사용하기
yhat_test = model.predict(x_test, batch_size=32)

import matplotlib.pyplot as plt

plt_row = 5
plt_col = 5

plt.rcParams["figure.figsize"] = (10, 10)

f, axarr = plt.subplots(plt_row, plt_col)

cnt = 0
i = 0

while cnt < (plt_row * plt_col):

    if np.argmax(y_test[i]) == np.argmax(yhat_test[i]):
        i += 1
        continue

    sub_plt = axarr[cnt / plt_row, cnt % plt_col]
    sub_plt.axis('off')
    sub_plt.imshow(x_test[i].reshape(width, height))
    sub_plt_title = 'R: ' + str(np.argmax(y_test[i])) + ' P: ' + str(np.argmax(yhat_test[i]))
    sub_plt.set_title(sub_plt_title)

    i += 1
    cnt += 1

plt.show()

# 7. 수행결과
# [0.03347810361186821, 0.9902999997138977]