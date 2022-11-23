#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

## 예제 2-1 시리즈 멤버 알아보기

sr = pd.Series([1,2,3,4],index=list('abcd'),name="SR1")

sr

sr.name

sr.dtype

sr.shape

sr.ndim

sr.size

sr.index


# In[3]:


import pandas as pd

## 예제 2-2 데이터프레임 멤버 알아보기

df = pd.DataFrame([[1,2,3,4],[5,6,7,8]],index=['a','b'],
                  columns=['c1','c2','c3','c4'])

df

df.shape

df.ndim

df.size

df.index

df.columns

df.info()


# In[4]:


import pandas as pd

## 예제 2-3 시리즈와 데이터프레임의 다양한 멤버 확인하기

dir(pd.Series)

s = set([ i for i in dir(pd.Series) if not i.startswith("_")])

s

dir(pd.DataFrame)

d = set([ i for i in dir(pd.DataFrame) if not i.startswith("_")])

d


# In[5]:


import pandas as pd

## 예제 2-4 파일에 저장된 멤버 정보를 읽어와서 확인하기

df_f = pd.read_csv('../data/series_dataframe.csv', 
                   usecols=['Member','Series','DataFrame'],
                   encoding='euc-kr')

df_f.head()

 # 1행을 헤더로 사용하였기 때문에 전체 데이터는 헤더를 제외한 264가 된다.

df_f.shape

df_f['Series'].head()

# Series 열에 데이터가 없는 셀의 총합

df_f['Series'].isnull().sum()

df_f['Series'].head(15)

df_f['DataFrame'].isnull().sum()

(df_f['Member'] == df_f['Series']).head()


# In[6]:


## 예제 2-5 : 리스트로 시리즈 생성

import pandas as pd

obj = pd.Series([1,2,3,4])


obj

obj.values

# start ~ stop-1

obj.index

obj.dtype


# In[7]:


import pandas as pd

## 예제 2-6 : 딕셔너리로 시리즈 생성

d = {'a':1,'b':2,'c':3}
ser = pd.Series(d,name='something')

ser

index = ['a','b','c']

obj1 = pd.Series([1,2,3],index=index,name="test") 

obj1


# In[8]:


import pandas as pd

## 예제 2-7 : 넘파이 모듈 이용해서 생성하기

import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5))

# randn method는 표준 정규분포 확률을 따르는 난수를 return

# 표준정규분포란 평균을 0, 표준편차를 1인 정규분포를 의미

s


# In[9]:


import pandas as pd

## 예제 2-8 : 시리즈의 기본 속성 알아보기

obj = pd.Series([1,2,3,4],name="obj")

obj.shape, obj.ndim

obj

obj.values

obj.dtype, obj.nbytes

obj_emp = pd.Series()

obj_emp.empty


# In[10]:


import pandas as pd

## 예제 2-9 : 시리즈로 데이터프레임 생성


s1 = pd.Series([1,2,3,4],name='s1')
s2 = pd.Series(['a','b','c','d'],name='s2')

s1

s2

df = pd.DataFrame({'s1':s1,'s2':s2})

# dict인 경우 키가 열로 들어감

df

df['s1']

s1 == df['s1']

# dict가 아닌 경우 시리즈의 이름이 행 한위로 들어감
# 다음 다음의 예제와 같은 원리

df_a = pd.DataFrame([s1,s2])

df_a

df_b = pd.DataFrame(
    [
        [1,2,3,4],
        ['a','b','c','d']
    ]
)
df_b


# In[ ]:


import pandas as pd

## 예제 2-10 : 딕셔너리가 원소인 딕셔너리로 데이터프레임 생성

# dict 키는 열로 지정 값이 중첩된 dict라면 여기에서의 키는 각각 행의 이름으로 매칭

data = {'AAA' : {'a' : 4,'b':5, 'c':6, 'd':7}, 
        'BBB' : {'a': 10, 'b' : 20, 'c':30, 'd': 40},
        'CCC' : {'a':100, 'b': 50, 'c': -30, 'd': -50} }

df = pd.DataFrame(data)

df

# 컬럼을 재정의하여 기존의 DataFrame을 필터링

df2 = pd.DataFrame(data, columns=['AAA','CCC'])

df2


# In[12]:


import pandas as pd

## 예제 2-11 : 데이터 프레임의 기본 속성 알아보기

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names,births))


BabyDataSet

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])

df

df.values

df.axes

df.index

df.columns

df.dtypes

df.shape, df.ndim, df.size


# In[13]:


import pandas as pd

## 예제 2-12 데이터를 읽어오기

ct = pd.read_csv("../data/2017_college_tuition.csv",encoding='euc-kr')

ct.head()

ct.tail()

ct.shape

ct.columns

## 예제 2-13 대괄호를 이용한 일반 검색

ct_ser = ct['학교명']

ct_ser.head()

ct_ser[0]

ct_ser[1]

ct_ser[100]

ct_ser.__getitem__(100)

ct.__getitem__('학교명').head()



## 예제 2-14 대괄호를 이용한 슬라이스 검색

ct_ser[10:20]

ct_slice = ct[10:20]

ct_slice

ct_slice.head()

ct_slice.shape

# slice => [] 와 같은 효과

ct.__getitem__(slice(10,20)).head()

