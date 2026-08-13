nums = [5,1,6,3,9,4,8,2]

large = nums[0]

for i in range(0, len(nums)):

    if nums[i] > large:
        large = nums[i]

print(large)