number3 = []
number5 = []
sum1 = 0
sum2 = 0

for num in range(1,1000):
    if num %3 == 0 :
        number3.append(num)
    elif num %5 == 0 :
        number5.append(num)
for num2 in number3:
    sum1 += num2
for num3 in number5:
    sum2 += num3

#print(number3)
#print(number5)
print(sum1+sum2)
