from itertools import product

list = [0,1,2,3]

for score in product(list,list):
    print(score)