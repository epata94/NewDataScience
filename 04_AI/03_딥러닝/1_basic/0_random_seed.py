import numpy as np

# seed 적용하기 전
print('seed 적용하기 전')
print('최초 데이터셋 생성')
print(f'데이터셋1: {np.random.rand(3)}')
print(f'데이터셋2: {np.random.rand(5)}')

print('데이터셋 재생성')
print(f'데이터셋1: {np.random.rand(3)}')
print(f'데이터셋2: {np.random.rand(5)}')

# seed 적용한 후
print('\nseed 적용한 후')
np.random.seed(0)
print('최초 데이터셋 생성')
print(f'데이터셋1: {np.random.rand(3)}')
print(f'데이터셋2: {np.random.rand(5)}')

np.random.seed(0)
print('데이터셋 재생성')
print(f'데이터셋1: {np.random.rand(3)}')
print(f'데이터셋2: {np.random.rand(5)}')
