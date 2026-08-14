nums = [5,1,6,3,9,4,8,2]

second_large = None 

for i in range(0, len(nums)):
    if second_large is None or nums[i] > second_large:
        if nums[i] != max(nums):
            second_large = nums[i]


print(second_large)