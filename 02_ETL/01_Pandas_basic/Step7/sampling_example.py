# 샘플링한 데이터를 원본에서 소진하는 예제
import pandas as pd
df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10], columns=['관측치'])

sampling_data = df.sample(3, random_state=100)
print('원본 데이터')
print(df)
print('\n샘플 데이터')
print(sampling_data)

df.drop(sampling_data.index,inplace=True)
print('\n원본 데이터')
print(df)