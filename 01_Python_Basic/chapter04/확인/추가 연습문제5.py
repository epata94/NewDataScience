point = {'kim99' : 12000,
         'lee66' : 11000,
         'han55' : 3000,
         'hong77' : 5000,
         'hwang33' : 18000}
num = 0
for id in point :
    num += 1
    print(f"{num}. 아이디: {id}, 마일리지: {point[id]}점")
