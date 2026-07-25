def bubble(nums):

    n = len(nums)
    for i in range(n-2, -1,-1):
        is_swap = False
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                is_swap = True
    if is_swap == False:
        return nums
arr = [5,1,6,3,9,4,8,2]
nums = [1, 2, 3, 4, 5, 6, 8, 9]
print(arr)
print(bubble(arr))
print(bubble(nums))