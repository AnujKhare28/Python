nums = [1,1,1,2,3,3,4,4,4,5,6,6,7,8,8,9,10]

n = len(nums)
i = 0
j = i + 1
if n == 1:
    print(1)

while j < n:
    if nums[i] != nums[j]:
        i += 1
        nums[i],nums[j] = nums[j], nums[i]
    j += 1

print(i+ 1)
print(nums)
