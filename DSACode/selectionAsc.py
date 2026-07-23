def selection(nums):
    n = len(nums)
    for i in range(0,n):
        mini_idx = i
        for j in range(i+1,n):
            if nums[j] < nums[mini_idx]:
                mini_idx = j
        nums[i], nums[mini_idx] = nums[mini_idx],nums[i]
    return nums

print(selection([5,7,8,4,1,2,3,9,6]))