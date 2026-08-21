nums = [5,1,6,3,9,4,8,2]


def linear(nums,target):
    for i in range(0,len(nums)):
        if nums[i] == target:
            return i
    return -1

print(linear(nums,9))