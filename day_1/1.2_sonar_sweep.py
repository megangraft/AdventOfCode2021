import requests

nums = open('1_input.txt').read().splitlines()

b = 0

first_sum = sum([int(x) for x in nums[0:3]])
second_sum = sum([int(x) for x in nums[1:4]])
increases = 0

for n in nums[:-4]:
    if second_sum > first_sum:
        increases += 1
    first_sum = first_sum - int(n) + int(nums[b+3])
    second_sum = second_sum - int(nums[b+1]) + int(nums[b+4])
    b += 1

# final two sums checked separately bc when variables are modified in the final loop, they become out of range
if second_sum > first_sum:
    increases += 1

print(increases)