point = {'kim99' : 12000,
         'lee66' : 11000,
         'han55' : 3000,
         'hong77' : 5000,
         'hwang33' : 18000}

TARGET_ID = 'han55'

point[TARGET_ID] = 5000

print(f"{TARGET_ID}님의 마일리지가 {point[TARGET_ID]}점으로 수정되었습니다")
print(f"{TARGET_ID}님의 마일리지가 {point.get(TARGET_ID)}점으로 수정되었습니다")
