import random

lotto = []
# 1, 3
for i in range(6):
    num = random.randint(1,45)

    while num in lotto:
        num = random.randint(1,45)

    lotto.append(num)

print(lotto)
