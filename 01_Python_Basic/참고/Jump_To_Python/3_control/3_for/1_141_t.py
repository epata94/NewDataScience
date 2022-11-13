total=0
for i in range(10):
#    print("%d "%i,end='')
    print(i,end=' ')
#    total = total + i
    total += i
print("\t\t => total: %d"%total)

total=0
for i in range(1,11):
    print("%d "%i,end='')
    total += i
print("\t\t => total: %d"%total)

total=0
for i in range(1,11,2):
    print("%d "%i,end='')
    total += i
print("\t\t\t => total: %d"%total)
