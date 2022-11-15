temperature = {'월':25.5,
               '화':28.3,
               '수':33.2,
               '목':32.1,
               '금':17.3,
               '토':35.3,
               '일':33.3}

temperatures = []

for i in temperature :
    temperatures.append(temperature[i])
#print(temperatures)
min_temp = min(temperatures)

print(f"가장 낮은 일간 최고 기온 : {min_temp}")
