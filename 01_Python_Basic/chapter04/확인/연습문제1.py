lst = [10,1,5,2]

result = lst * 2
print(f"단계1 : {result}")

result.append(lst[0] * 2)

print(f"단계2 : {result}")

result2 = []

n = 0

for i in result :
        if n%2 == 1:
                result2.append(i)
        n = n + 1
print(f"단계3 : {result2}")


