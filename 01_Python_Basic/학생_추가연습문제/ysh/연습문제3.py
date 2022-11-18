import sys

def myargv(number_list):
    result = 0
    for i in number_list:
        #print(int(i))
        result += int(i)
    return result
    
number_list = sys.argv[1:]
#print(number_list)
#myargv(number_list)
print(myargv(number_list))