import sys
nums=sys.argv[1:]

# print(nums)
def sum_of_all(nums):
    sum=0
    for num in nums:
        sum += int(num)
    print(sum)

sum_of_all(nums)