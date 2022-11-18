#
mylist = [1,-2,3,-5,8,-3]

result = list(filter((lambda x: x > 0),mylist))
print(result)