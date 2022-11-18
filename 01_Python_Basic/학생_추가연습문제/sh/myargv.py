import sys

def number_print(number_list):
    total = 0
    for number in number_list[1:]:
        total += int(number)
    print(total)

number_list = sys.argv[:]

number_list = ['test03_myargv.py',1,2,3,4,5,6,7,8,9,10]

number_print(number_list)