import random
len_list = int(input("vector 수 : "))
list = []
for i in range(0,len_list) :
    r = random.randint(1, 10)
    list.append(r)
    print(list[i])

print(f"vector 크기 : {len_list}")