nums = [5,7,8,4,1,2,3,9,6]

n = len(nums)

temp = nums[n - 1]

for i in range((n - 2), -1, -1):
    nums[i + 1] = nums[i]
nums[0] = temp

print(nums)