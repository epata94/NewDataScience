## 후처리

import pandas as pd


input_file = '초단기실황조회_202212250734.csv'

df = pd.read_csv(input_file)

print(df)


## 데이터 입력
# timestamp nx ny pty reh rn1 t1h uuu vec vvv wsd

df2 = pd.pivot_table(df,index='baseDate',columns=['category'], values='obsrValue')

print(df2)

# 생각해 볼 것