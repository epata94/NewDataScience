#4
import random

lotto = []
index = 0
while index < 6:
    lotto_num = random.randint(1,46)
    if lotto_num in lotto:
        continue
    else:
        lotto.append(lotto_num)
        index += 1

print(f'이번주 로또번호 {lotto}')
