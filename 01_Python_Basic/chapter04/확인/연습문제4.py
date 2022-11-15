position = ['과장','부장','대리','사장','대리','과장']

wc= {}
wc2 = []

#union = list(set(position))
#print(f"중복되지 않는 직위 :{union}")  #정답방법

for i in position :
    wc[i] = wc.get(i,0) + 1

for i in wc :
    wc2.append(i)

print(f"중복되지 않은 직위: {wc2}")
print(f"각 직위별 빈도수 :{wc}")



