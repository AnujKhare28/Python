def rotateByK3(nums, k):
    n = len(nums)
    def revArr(nums, l ,r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    revArr(nums,(n-k),(n-1))
    revArr(nums,0,(n-k-1))
    revArr(nums,0,(n-1))
    return nums
    
    
nums = [5,7,8,4,1,2,3,9,6]

print(rotateByK3(nums,2))