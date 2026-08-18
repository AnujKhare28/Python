def rotateByK2(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums

nums = [5,7,8,4,1,2,3,9,6]

print(rotateByK2(nums,4))