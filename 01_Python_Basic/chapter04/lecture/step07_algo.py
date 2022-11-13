# 1. 최댓값/최솟값

import random

dataset = []
for i in range(10) :
    r = random.randint(1,100)
    dataset.append(r)

print(dataset)

# 변수 초기화
vmax = vmin = dataset[0]

for i in dataset:
    if vmax < i:
        vmax = i
    if vmin > i:
        vmin = i

print('max =', vmax)
print('min =', vmin)

max_v = min_v = dataset[0]
size = len(dataset)  # data 길이
idx = 0

while idx < size:  # data 길이 반복
    if dataset[idx] > max_v:
        max_v = dataset[idx]
    if dataset[idx] < min_v:
        min_v = dataset[idx]

    idx += 1  # 카운터

print('max = %d, min = %d' % (max_v, min_v))  # max = 45, min = 2

# 2. 정렬

# (1) 오름차순 정렬
dataset = [3, 5, 1, 2, 4]
n = len(dataset)
for i in range(0, n-1) : # 1 ~ n-1
    for j in range(i+1, n) : # i+1 ~ n-1
        if dataset[i] > dataset[j] :
            tmp = dataset[i]
            dataset[i] = dataset[j] # 3 5
            dataset[j] = tmp
    print(dataset)

print(dataset) # [1, 2, 3, 4, 5]

# (2) 내림차순 정렬
dataset = [3, 5, 1, 2, 4]
n = len(dataset)
for i in range(0, n-1) : # 1 ~ n-1
    for j in range(i+1, n) : # i+1 ~ n-1
        if dataset[i] < dataset[j] :
            tmp = dataset[i]
            dataset[i] = dataset[j] # 3 5
            dataset[j] = tmp
    print(dataset)

print(dataset) # [5, 4, 3, 2, 1]


# 3. 검색
dataset = [5, 10, 18, 22, 35, 55, 75, 103]
value = int(input("검색할 값 입력 : "))

low = 0
high = len(dataset) - 1
loc = 0
state = False
while (low <= high):
    mid = (low + high) // 2

    if dataset[mid] > value:
        high = mid - 1
    elif dataset[mid] < value:
        low = mid + 1
    else: # 찾은 경우
        loc =  mid
        state = True
        break # 반복 exit

if state :
    print('찾은 위치 : %d 번째' %(loc+1))
else :
    print('찾는 값은 없습니다.')
