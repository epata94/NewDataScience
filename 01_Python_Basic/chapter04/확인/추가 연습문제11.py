temperature = {'월':25.5,
               '화':28.3,
               '수':33.2,
               '목':32.1,
               '금':17.3,
               '토':35.3,
               '일':33.3}
list = []
for i in temperature :
    if temperature[i] >= 30 :
        list.append(i)

#print(list)

for i in list:
    if i == '일' :
        print(i,end='')
    else :
       print(i,end=', ')

#print(f"{', '.join(list)}") #솔루션 방법
