import random

num_list = []
#print(len(num_list))

while len(num_list) < 6:
    random_number = int(random.randint(1,46))
    if random_number in num_list:
        #print(f"중복숫자 : {random_number}")
        # num_list.sort()
        continue
    else:
        num_list.append(random_number)

print(num_list)
