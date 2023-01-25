# 0. 사용할 패키지 불러오기
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
plt.style.use('ggplot')

# 랜덤시드 고정시키기
np.random.seed(5)

# 1. 데이터 준비하기
dataset = np.loadtxt("pima-indians-diabetes.data", delimiter=",")
# 1. Number of times pregnant
# 2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test
# 3. Diastolic blood pressure (mm Hg)
# 4. Triceps skin fold thickness (mm)
# 5. 2-Hour serum insulin (mu U/ml)
# 6. Body mass index (weight in kg/(height in m)^2)
# 7. Diabetes pedigree function
# 8. Age (years)
# 9. Class variable (0 or 1)

# 2. 데이터셋 생성하기
x_train = dataset[:700,0:8]
y_train = dataset[:700,8]
x_test = dataset[700:,0:8]
y_test = dataset[700:,8]

# 3. 모델 구성하기
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 4. 모델 학습과정 설정하기
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
optimizer_list=[]
# 기본 sgd
optimizer_list.append(['SGD',optimizers.SGD()])
# momentum
optimizer_list.append(['Momentum',optimizers.SGD(momentum=0.9)])
# NAG
optimizer_list.append(['NAG',optimizers.SGD(momentum=0.9, nesterov=True)])
# Adagrad
optimizer_list.append(['Adagrad',optimizers.adagrad()])
# RMSProp
optimizer_list.append(['RMSProp',optimizers.rmsprop()])
# AdaDelta
optimizer_list.append(['AdaDelta',optimizers.adadelta()])
# Adam
optimizer_list.append(['Adam',optimizers.adam()])
#Nadam
optimizer_list.append(['Nadam',optimizers.nadam()])

score_list=[]
opt_name_list=[]
for optimizer_element in optimizer_list:
    model.compile(loss='binary_crossentropy', optimizer=optimizer_element[1], metrics=['accuracy'])

    # 5. 모델 학습시키기
    model.fit(x_train, y_train, epochs=1500, batch_size=64)

    # 6. 모델 평가하기
    scores = model.evaluate(x_test, y_test)
    score = scores[1]*100
    opt_name = optimizer_element[0]
    print("Optimizer: %s %s: %.2f%%" %(opt_name, model.metrics_names[1], score))
    score_list.append(score)
    opt_name_list.append(opt_name)

# 7. 결과
font_location = "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font',family=font_name)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
optimizer_index =range(len(optimizer_list))
ax1.bar(optimizer_index, score_list, align='center', color='darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(optimizer_index, opt_name_list, color='red', fontsize='large')

plt.xlabel('Optimizer Name')
plt.ylabel('Accuracy')
plt.title('SGD ~ Nadam 까지 기본 성능 비교 ')
plt.savefig('SGD_to_Nadam.png', dpi=400)
plt.show()