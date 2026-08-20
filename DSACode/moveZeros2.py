nums = [0,1,0,2,0,3,0,4,0,0,5,6,0,0,7,8]

if len(nums) == 1:
    print(nums)
i = 0
while i < len(nums):
    if nums[i] == 0:
        break
    i +=1
if i == len(nums):
    print(nums)
j = i+1
while j < len(nums):
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
    j += 1

print(nums)
