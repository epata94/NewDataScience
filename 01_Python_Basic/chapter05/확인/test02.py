def average(num):
    total=0
    for n in num:
        total+=n
    return total/len(num)

num_list=input("공백을 두고 원하는 만큼 숫자를 입력 하여 주세요 : ").split()
num_list=list(map(int,num_list))
average=average(num_list)
print(average)