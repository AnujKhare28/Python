def rotateByK(nums, k):
    n = len(nums)
    rotate = k % n

    for i in range(0, rotate):
        e = nums.pop()
        nums.insert(0,e)
    return nums

nums = [5,7,8,4,1,2,3,9,6]

print(rotateByK(nums,10))


