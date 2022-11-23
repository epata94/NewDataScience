#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

## 예제 1-8 결측값으로 인스턴스 생성

import numpy as np

df_na = pd.DataFrame([1,2,np.nan])

df_na

df_na.sum()

# skipna 은 기본 값이 True이며 False로 명시적으로 주어졌을 경우 NaN을 포함하며 연산을 한다.
# 이때 모든 NaN 값의 연산은 NaN으로 표기함

df_na.sum(skipna=False)

df_na < 3

df_na <2

df_na < np.nan

df_na > np.nan

# 비교 연산은 결측값(누락값)에서 사용할 수 없다.

df_na == np.nan


# In[2]:


import pandas as pd

## 예제 1-9 축(Axis) 알아보기

df_sax = pd.Series([1,2,3,4])

df_sax

# axis=0 행(세로 방향), axis=1 열(가로방향)

# 시리즈는 기본 적으로 행에 대한 계산을 함

df_sax.sum(axis=0)

df_dax = pd.DataFrame([[1,2,3,4],[5,6,7,8]])

df_dax

# 행을 고정하여 0열 ~ 3열 까지의 모든 행의 sum() 값을 순차적으로 보여줌

df_dax.sum(axis=0)

# 열을 고정하여 0행, 1행의 sum() 값을 순차적으로 보여줌

df_dax.sum(axis=1)


# In[ ]:


import pandas as pd

## 예제 1-10 내부 원소 처리 기준

import numpy as np

# 1~10까지의 임의의 수를 3*3 배열에 생성한다.

np.random.randint(1,10,(3,3))

df_1 = pd.DataFrame(np.random.randint(1,10,(3,3)),columns=list('ABC'))

df_1



df_2 = pd.DataFrame(np.random.randint(1,10,(3,3)),columns=list('CAB'))

df_2

# 현재의 프레임은 유지되면서 각종 연산함수의 값이 각각의 원소에 업데이트 한다.

np.log(df_2)

df_2

# 열을 맞추어 계산한다. 

df_1 + df_2

df_3 = pd.DataFrame(np.random.randint(1,10,(3,2)),columns=list('CB'))

df_3

#df_3는 A열이 없으므로 없는 값(nan)과의 연산으로 A열의 모든 값은 NaN이 된다.

df_1 + df_3


# In[ ]:


import pandas as pd



## 예제 1-11 한글 인코딩 알아보기

get_ipython().system('pip install chardet')

import chardet

def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc

my_encoding1 = find_encoding('../data/weight_loss.csv')
df_1 = pd.read_csv('../data/weight_loss.csv', encoding=my_encoding1)

my_encoding1

try :
    pd.read_csv('../data/weight_loss.csv', encoding="utf-8")
    
except Exception as e :
    print(e)

df_1.head()

my_encoding2 = find_encoding('../data/korea_movie_list.csv')
df_2 = pd.read_csv('../data/korea_movie_list.csv', encoding=my_encoding2)

my_encoding2

try :
    pd.read_csv('../data/korea_movie_list.csv', encoding="utf-8")
    
except Exception as e :
    print(e)

df_2.head(2)



df_3 = pd.read_csv('../data/korea_movie_list.csv', engine='python')

df_3.head(2)



try :
    pd.read_csv('../data/korea_movie_list.csv', engine='c')
except Exception as e :
    print(e)



url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/attention.csv'

df_att = pd.read_csv(url,error_bad_lines=False)

df_att.head()

df_att.drop('Unnamed: 0',axis=1).head()

