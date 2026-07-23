def selection(nums):
    n = len(nums)
    for i in range(0,n):
        max_idx = i
        for j in range(i+1,n):
            if nums[j] > nums[max_idx]:
                max_idx = j
        nums[i], nums[max_idx] = nums[max_idx],nums[i]
    return nums

print(selection([5,7,8,4,1,2,3,9,6]))