point = {'kim99' : 12000,
         'lee66' : 11000,
         'han55' : 3000,
         'hong77' : 5000,
         'hwang33' : 18000}

score = []

for i in point :
    score.append(point[i])
#print(score)
hight = max(score)
#print(hight)
for id in point :
     point[id] == hight
    #max_id = id  #솔루션 방법
#print(f"{id}{hight}")
print(f"{id}님의 {hight}점이 가장 높은 점수입니다")



