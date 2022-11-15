temperature = {'월':25.5,
               '화':28.3,
               '수':33.2,
               '목':32.1,
               '금':17.3,
               '토':35.3,
               '일':33.3}
total = 0

for i in temperature :
    total += temperature[i]

#print(total)
avg = total / len(temperature)

#print("일주일간 최고 기온 평균 : %.1f" % avg)
print(f"일주일간 최고 기온 평균 :", format(avg,"3.1f"))