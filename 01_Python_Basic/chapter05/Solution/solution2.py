def average(num_list):
    total=0
    for num in num_list:
        total+=int(num)
    return total/len(num_list)

num_list=input("만큼 숫자를 입력 하여 주세요. 예) 10 20 15 30 7: ").split()
average=average(num_list)
print(average)