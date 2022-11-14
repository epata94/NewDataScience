position = ['과장', '부장', '대리', '사장','대리', '과장']
wc = {}

for key in position:
    # get()함수 : key 이용 value 가져오기
    wc[key] = wc.get(key, 0) + 1  # get() 이용

print(wc)