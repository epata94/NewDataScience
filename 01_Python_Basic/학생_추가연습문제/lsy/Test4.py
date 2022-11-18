import random
lotto=[]
i=0
while i<6:
    rand_num=random.randint(1,7)
    if rand_num not in lotto:
        lotto.append(rand_num)
        i += 1
print(f'출력값: {lotto}')

