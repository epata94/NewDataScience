#3
import sys

nums = sys.argv[1:]
def num_allAdd(nums):
    sum = 0
    for num in nums:
        sum += int(num)

    return sum

sum = num_allAdd(nums)
print(sum)
