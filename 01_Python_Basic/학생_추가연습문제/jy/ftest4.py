#4.	random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자(단 중복된 숫자가 있으면 안 됨). Find,in (중복)
import random

lotto = []

while True:
    r = random.randint(1, 45)
    if r not in lotto:
        lotto.append(r)

    if len(lotto) == 6:
        break

print(f"로또 당청번호는 ~!! {lotto} 입니다~~~!!! ")