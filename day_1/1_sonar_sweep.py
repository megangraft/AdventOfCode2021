import requests

nums = open('1_input.txt').read().splitlines()

b = 1
increases = 0

for n in nums[:-1]:
    if int(nums[b]) > int(n):
        increases += 1
    b += 1

print(increases)