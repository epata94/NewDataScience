import sys

args = sys.argv[:]
argss = args[1:]
argss = list(map(int,argss))

# print(argss)

sum = 0
for argument in argss:
    sum += argument

print(sum)



