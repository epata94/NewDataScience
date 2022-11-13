'''
matplotlib API 사용 차트 그리기 
 matplotlib 패키지 install
c:\Python36] pip install matplotlib
C:\Python36\Lib\site-packages\matplotlib 패키지 확인 

  형식) plt.plot(data); plt.show()
  1. 기본 차트 그리기 
  2. 산점도 그리기 
  3. 차트 플롯으로 여러 개 차트 그리기 
  4. 차트 플롯으로 한 개 차트 그리기
'''

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:24:52 2019

차트 그리기 
 1. 기본 차트 그리기 
 2. 산점도 그리기 
 3. subplot 이용 차트 그리기  
"""
import matplotlib.pyplot as plt  # 차트 생성
import random # 차트 자료 생성
# 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# 차트 자료 생성
print(random.randint(a=1, b=5))  # 1~5
print(random.random())  # 0.2730656194499087 : 0~1
print(random.normalvariate(mu=0, sigma=1))  # 1.1086376820835209 - 표준정규분포

# plot()함수 도움말
help(plt.plot)
'''
plot(x, y)        # plot x and y using default line style and color
plot(x, y, 'bo')  # plot x and y using blue circle markers
plot(y)           # plot y using x as index array 0..N-1
plot(y, 'r+')     # ditto, but with red plusses
'''

# 1. 기본 차트 그리기

# (1) 1개 data
data = range(10)  # range(n) 동일 - 0~9
data

plt.plot(data)  # plot(y), x : index
plt.show()  # show() 생략 가능
plt.plot(data, 'r+')  # plot(y, 'r+')

# (2) 2개 data
data2 = [random.random() for i in range(10)]
plt.plot(data, data2)  # line
plt.plot(data, data2, 'ro')  # point

# 2. 산점도 그리기
# (1) 단색 산점도
plt.scatter(x=data, y=data2, c='b', marker='o')

# (2) 여러가지 색 산점도
cdata = [random.randint(a=1, b=3) for i in range(10)]
cdata  # [3, 2, 2, 1, 3, 2, 3, 1, 3, 3]
plt.scatter(x=data, y=data2, c=cdata, marker='o')

# 3. 히스토그램
data3 = [random.normalvariate(mu=0, sigma=1) for i in range(1000)]
plt.hist(data3) # 정규분포

data4 = [random.uniform(a=1, b=100) for i in range(1000)]
plt.hist(data4) # 균등분포

# 4. 차트 크기 지정
help(plt.figure)
fig = plt.figure(figsize=(12, 5))  # (w, h)
chart = fig.add_subplot(1, 1, 1)

data4 = [random.random() for i in range(50)]
data5 = [random.random() for i in range(50)]

chart.plot(data4, color='r', label='step', drawstyle='steps-post')
chart.plot(data5, color='b', label='line')

# 차트 구성요소 추가
plt.title("step and line graph")  # 제목
plt.xlabel("index")  # x축 이름
plt.ylabel("random number")  # y축 이름
plt.legend(loc='best')  # 범례

'''
exam03
'''




