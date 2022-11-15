list = [1,3,5,4,2]
n = len(list)
for i in range(0, n-1) :
    for j in range (i+1 , n) :
        if list[i] > list[j]:
            tmp = list[i]
            list[i]=list[j]
            list[j] = tmp
print(list)
