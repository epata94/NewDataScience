import sys

lst = sys.argv[1:]

sum = 0

for n in lst :
    sum += int(n)

print(sum)